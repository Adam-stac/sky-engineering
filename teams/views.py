from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Dependency, EngineeringTeam, TeamStaffAllocation

from .forms import TeamMeetingRequestForm
from .models import TeamMeetingRequest


# Name:
# Student ID:
# Student: Student 1
# Feature: Team page


def _build_team_skills(team):
    # Build a small list of useful skills from the team members and repositories.
    skills = []

    for allocation in team.members.all():
        engineer_profile = getattr(allocation.user, "engineer", None)
        # Use the engineer specialisation when it is available.
        if engineer_profile and engineer_profile.specialisation:
            skills.append(engineer_profile.specialisation)
        # Also include the role the member has inside the team.
        if allocation.role_in_team:
            skills.append(allocation.role_in_team)

    for repository in team.repositories.all():
        # Repository language helps show the technical skills the team uses.
        if repository.primary_language:
            skills.append(repository.primary_language)

    cleaned_skills = []
    for skill in skills:
        normalised_skill = skill.strip()
        # Keep only non-empty values and remove duplicates.
        if normalised_skill and normalised_skill not in cleaned_skills:
            cleaned_skills.append(normalised_skill)

    return cleaned_skills[:8]


@login_required
def team_list(request):
    # Show all teams and allow the user to search team, department, or manager details.
    if request.method == "POST":
        # The hidden team_id tells us which team the meeting was made for.
        team = get_object_or_404(EngineeringTeam, pk=request.POST.get("team_id"))
        form = TeamMeetingRequestForm(request.POST)
        if form.is_valid():
            # Save the meeting only after linking it to the team and current user.
            meeting_request = form.save(commit=False)
            meeting_request.team = team
            meeting_request.requested_by = request.user
            meeting_request.save()
            messages.success(
                request,
                f"Meeting request saved for {team.team_name}.",
            )
            return redirect("teams:list")
        messages.error(request, "Please fix the meeting form errors below.")
    else:
        form = TeamMeetingRequestForm()

    # The same page also supports searching across team-related information.
    search_query = request.GET.get("q", "").strip()
    teams_queryset = (
        EngineeringTeam.objects.select_related("department", "manager")
        .prefetch_related(
            Prefetch(
                "members",
                queryset=TeamStaffAllocation.objects.select_related("user__engineer"),
            ),
            "repositories",
            Prefetch(
                "upstream_dependencies",
                queryset=Dependency.objects.select_related("target_team"),
            ),
            Prefetch(
                "downstream_dependencies",
                queryset=Dependency.objects.select_related("source_team"),
            ),
        )
        .order_by("team_name")
    )

    if search_query:
        # Search across the main fields a user may know about a team.
        teams_queryset = teams_queryset.filter(
            Q(team_name__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(mission__icontains=search_query)
            | Q(purpose__icontains=search_query)
            | Q(responsibilities__icontains=search_query)
            | Q(department__department_name__icontains=search_query)
            | Q(manager__username__icontains=search_query)
            | Q(manager__first_name__icontains=search_query)
            | Q(manager__last_name__icontains=search_query)
            | Q(contact_email__icontains=search_query)
            | Q(slack_channel__icontains=search_query)
            | Q(teams_channel__icontains=search_query)
            | Q(members__user__username__icontains=search_query)
            | Q(members__user__first_name__icontains=search_query)
            | Q(members__user__last_name__icontains=search_query)
            | Q(members__role_in_team__icontains=search_query)
            | Q(repositories__repository_name__icontains=search_query)
            | Q(repositories__primary_language__icontains=search_query)
            | Q(upstream_dependencies__target_team__team_name__icontains=search_query)
            | Q(downstream_dependencies__source_team__team_name__icontains=search_query)
        ).distinct()

    teams = list(teams_queryset)
    for index, team in enumerate(teams, start=1):
        # Add a few extra values used only by the template.
        team.skill_tags = _build_team_skills(team)
        team.email_target = team.contact_email or getattr(team.manager, "email", "")
        team.accordion_id = f"team-panel-{team.id}"
        team.heading_id = f"team-heading-{team.id}"
        # Open the first result after a search so the page feels easier to use.
        team.show_expanded = bool(search_query) and index == 1

    # Show the latest meeting requests at the top of the page.
    recent_meetings = TeamMeetingRequest.objects.select_related(
        "team", "requested_by"
    ).order_by("scheduled_for")[:8]

    context = {
        "page_title": "Teams",
        "page_sub": "Browse engineering teams, contact them, and review their dependencies.",
        "teams": teams,
        "search_query": search_query,
        "meeting_form": form,
        "recent_meetings": recent_meetings,
    }
    return render(request, "teams/team_list.html", context)
