<<<<<<< HEAD
# Name: Ayaan Surani
# Student ID: W2070551
# Student: Student 3
# Feature: Messages
# Contribution: Individual work for testing the main messaging workflows.

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Message


class MessageViewsTests(TestCase):
    def setUp(self):
        # Create two users to test sending and receiving messages.
        user_model = get_user_model()
        self.sender = user_model.objects.create_user(
            username="sender",
            password="testpass123",
            first_name="Send",
            last_name="Er",
        )
        self.recipient = user_model.objects.create_user(
            username="recipient",
            password="testpass123",
            first_name="Rec",
            last_name="Iver",
        )
        self.client.login(username="sender", password="testpass123")

    def test_user_can_save_draft_without_recipient(self):
        # A draft should save even if it is not complete.
        response = self.client.post(
            reverse("messages_app:new"),
            {
                "subject": "Draft subject",
                "body": "",
                "save_draft": "1",
            },
        )

        self.assertRedirects(response, reverse("messages_app:drafts"))
        draft = Message.objects.get()
        self.assertEqual(draft.status, Message.STATUS_DRAFT)
        self.assertIsNone(draft.recipient)

    def test_send_requires_complete_message(self):
        # A message should not send if the important fields are empty.
        response = self.client.post(
            reverse("messages_app:new"),
            {
                "subject": "",
                "body": "",
                "send_message": "1",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Choose a recipient before sending.")
        self.assertContains(response, "Add a subject before sending.")
        self.assertContains(response, "Write a message before sending.")
        self.assertEqual(Message.objects.count(), 0)

    def test_sent_message_appears_in_sender_and_recipient_mailboxes(self):
        # After sending, the message should appear in both users' mailbox pages.
        response = self.client.post(
            reverse("messages_app:new"),
            {
                "recipient": self.recipient.pk,
                "subject": "Production issue",
                "body": "Please review the latest deployment update.",
                "send_message": "1",
            },
        )

        message_obj = Message.objects.get()
        self.assertRedirects(response, reverse("messages_app:detail", kwargs={"pk": message_obj.pk}))
        self.assertEqual(message_obj.status, Message.STATUS_SENT)
        self.assertIsNotNone(message_obj.sent_at)

        sent_response = self.client.get(reverse("messages_app:sent"))
        self.assertContains(sent_response, "Production issue")

        self.client.logout()
        self.client.login(username="recipient", password="testpass123")
        inbox_response = self.client.get(reverse("messages_app:inbox"))
        self.assertContains(inbox_response, "Production issue")

    def test_opening_received_message_marks_it_as_read(self):
        # Opening a message should change it from unread to read.
        message_obj = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            subject="Project update",
            body="This is the latest message.",
            status=Message.STATUS_SENT,
        )
        message_obj.mark_as_sent()
        message_obj.save()

        self.client.logout()
        self.client.login(username="recipient", password="testpass123")
        self.client.get(reverse("messages_app:detail", kwargs={"pk": message_obj.pk}))

        message_obj.refresh_from_db()
        self.assertTrue(message_obj.is_read)
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
