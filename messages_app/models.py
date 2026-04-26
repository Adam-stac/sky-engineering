<<<<<<< HEAD
# Name: Ayaan Surani
# Student ID: W2070551
# Student: Student 3
# Feature: Messages
# Contribution: Individual work for the messaging model used by inbox, sent, drafts, and message detail.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Message(models.Model):
    # A message can be saved as a draft first and sent later.
    STATUS_DRAFT = "draft"
    STATUS_SENT = "sent"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_SENT, "Sent"),
    ]

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
        null=True,
        blank=True,
    )
    subject = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    # This tells us if the message is still a draft or has been sent.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    # This is used to show if the receiver has opened the message.
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # We store the sent time separately so it can be shown in the inbox and sent pages.
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        # Show the newest messages first.
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        subject = self.subject or "Untitled message"
        return f"{self.sender} -> {self.recipient or 'Draft'}: {subject}"

    def mark_as_sent(self):
        # This updates the fields when a draft is sent.
        self.status = self.STATUS_SENT
        self.sent_at = timezone.now()
        self.is_read = False

    @property
    def mailbox_timestamp(self):
        # Sent messages show sent time, but drafts show the latest saved time.
        return self.sent_at or self.updated_at or self.created_at
=======
from django.db import models

# Create your models here.
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
