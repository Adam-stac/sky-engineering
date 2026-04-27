# Name: Ayaan Surani
# Student ID: W2070551
# Student: Student 3
# Feature: Messages
# Contribution: Individual work for the compose message and draft form validation.

from django import forms

from core.models import User

from .models import Message


class MessageForm(forms.ModelForm):
    # This form is used for both new messages and editing drafts.
    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]
        widgets = {
            "recipient": forms.Select(attrs={"class": "form-select"}),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter a message subject"}
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "Write your message here",
                }
            ),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        recipient_field = self.fields["recipient"]
        # The user can leave this empty while saving a draft.
        recipient_field.required = False
        # Do not allow the user to send a message to themselves.
        recipient_field.queryset = User.objects.exclude(pk=getattr(user, "pk", None)).order_by(
            "first_name", "last_name", "username"
        )
        # These are allowed to be empty for drafts.
        self.fields["subject"].required = False
        self.fields["body"].required = False

    def validate_for_send(self):
        # When sending, all important fields must be filled in.
        valid = True
        if not self.cleaned_data.get("recipient"):
            self.add_error("recipient", "Choose a recipient before sending.")
            valid = False
        if not self.cleaned_data.get("subject", "").strip():
            self.add_error("subject", "Add a subject before sending.")
            valid = False
        if not self.cleaned_data.get("body", "").strip():
            self.add_error("body", "Write a message before sending.")
            valid = False
        return valid
