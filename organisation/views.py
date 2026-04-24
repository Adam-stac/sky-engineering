from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Department, EngineeringTeam, Dependency


@login_required
def org_home(request):
    context = {
        'total_departments': Department.objects.count(),
        'total_teams': EngineeringTeam.objects.count(),
        'total_dependencies': Dependency.objects.count(),
    }
    return render(request, 'organisation/org_home.html', context)


@login_required
def department_list(request):
    departments = Department.objects.prefetch_related('teams').select_related('leader').all()
    context = {
        'departments': departments,
    }
    return render(request, 'organisation/department_list.html', context)


@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teams = EngineeringTeam.objects.filter(department=department).select_related('manager')
    context = {
        'department': department,
        'teams': teams,
        'team_count': teams.count(),
    }
    return render(request, 'organisation/department_detail.html', context)


@login_required
def team_type_list(request):
    pass


@login_required
def dependency_list(request):
    dependencies = Dependency.objects.select_related(
        'source_team', 'target_team',
        'source_team__department', 'target_team__department'
    ).all()
    context = {
        'dependencies': dependencies,
    }
    return render(request, 'organisation/dependency_list.html', context)


@login_required
def org_chart(request):
    pass