<<<<<<< HEAD
# Name: Ayaan Surani
# Student ID: W2070551
# Student: Student 3
# Feature: Messages
# Contribution: Individual work for routing the messaging pages.

=======
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
<<<<<<< HEAD
    # Main messages link.
    path("", views.index, name="index"),
    # Mailbox pages.
    path("inbox/", views.inbox, name="inbox"),
    path("sent/", views.sent_messages, name="sent"),
    path("drafts/", views.drafts, name="drafts"),
    # Page for writing a message.
    path("new/", views.new_message, name="new"),
    # Page for editing a saved draft.
    path("drafts/<int:message_id>/edit/", views.new_message, name="edit_draft"),
    # Page for viewing one message.
    path("<int:pk>/", views.message_detail, name="detail"),
]
=======
]
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
