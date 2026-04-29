from django import forms
from django.utils import timezone

from .models import TeamMeetingRequest


# Name:
# Student ID:
# Student: Student 1
# Feature: Team page forms


class TeamMeetingRequestForm(forms.ModelForm):
    # This form is shown on the Team page when a user schedules a meeting.
    class Meta:
        model = TeamMeetingRequest
        fields = ["title", "scheduled_for", "platform", "message"]
        widgets = {
            # These widgets make the form easier to use on the Team page.
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Example: Incident review"}
            ),
            "scheduled_for": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "platform": forms.Select(attrs={"class": "form-select"}),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Add a short meeting note for the team.",
                }
            ),
        }

    def clean_scheduled_for(self):
        scheduled_for = self.cleaned_data["scheduled_for"]
        # Keep users from booking a meeting in the past by mistake.
        if scheduled_for <= timezone.now():
            raise forms.ValidationError("Choose a future date and time for the meeting.")
        return scheduled_for
