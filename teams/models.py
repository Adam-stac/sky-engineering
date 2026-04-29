from django.conf import settings
from django.db import models

from core.models import EngineeringTeam


# Name:
# Student ID:
# Student: Student 1
# Feature: Team menu item and team meeting requests


class TeamMeetingRequest(models.Model):
    # This model stores meeting requests made from the Team page.
    PLATFORM_CHOICES = [
        ("teams", "Microsoft Teams"),
        ("zoom", "Zoom"),
        ("meet", "Google Meet"),
        ("phone", "Phone call"),
    ]

    team = models.ForeignKey(
        EngineeringTeam,
        on_delete=models.CASCADE,
        related_name="meeting_requests",
    )
    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="team_meeting_requests",
    )
    title = models.CharField(max_length=150)
    scheduled_for = models.DateTimeField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Show the nearest upcoming meeting first.
        ordering = ["scheduled_for", "-created_at"]

    def __str__(self):
        return f"{self.team.team_name} meeting on {self.scheduled_for:%Y-%m-%d %H:%M}"
