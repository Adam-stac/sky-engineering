from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ["title", "date", "time", "platform", "message"]
        widgets = {
         "title": forms.TextInput(attrs={"class": "form-control"}),
         "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
         "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
         "platform": forms.Select(attrs={"class": "form-control"}),
         "message": forms.Textarea(attrs={"class": "form-control"}),
 }