<<<<<<< HEAD
# Name: Ayaan Surani
# Student ID: W2070551
# Student: Student 3
# Feature: Messages
# Contribution: Individual work for inbox, sent, drafts, new message, send message, and message detail views.

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MessageForm
from .models import Message


def _mailbox_counts(user):
    # This is used on different pages to show inbox, sent, and draft counts.
    return {
        "inbox_count": Message.objects.filter(
            recipient=user,
            status=Message.STATUS_SENT,
        ).count(),
        "unread_count": Message.objects.filter(
            recipient=user,
            status=Message.STATUS_SENT,
            is_read=False,
        ).count(),
        "sent_count": Message.objects.filter(
            sender=user,
            status=Message.STATUS_SENT,
        ).count(),
        "draft_count": Message.objects.filter(
            sender=user,
            status=Message.STATUS_DRAFT,
        ).count(),
    }


def _folder_context(user, active_folder, page_title, page_sub, queryset):
    # This helper keeps the folder pages using the same layout and data.
    context = {
        "active_folder": active_folder,
        "page_title": page_title,
        "page_sub": page_sub,
        "messages_list": queryset,
    }
    context.update(_mailbox_counts(user))
    return context


@login_required
def index(request):
    # Open the inbox first when the user clicks Messages.
    return redirect("messages_app:inbox")


@login_required
def inbox(request):
    # Show messages sent to the current user.
    queryset = Message.objects.filter(
        recipient=request.user,
        status=Message.STATUS_SENT,
    ).select_related("sender", "recipient")
    context = _folder_context(
        request.user,
        "inbox",
        "Messages",
        "Review incoming updates and open conversations with your teammates.",
        queryset,
    )
    return render(request, "messages_app/message_list.html", context)


@login_required
def sent_messages(request):
    # Show messages the current user has sent.
    queryset = Message.objects.filter(
        sender=request.user,
        status=Message.STATUS_SENT,
    ).select_related("sender", "recipient")
    context = _folder_context(
        request.user,
        "sent",
        "Sent Messages",
        "Track the messages you have already delivered to other users.",
        queryset,
    )
    return render(request, "messages_app/message_list.html", context)


@login_required
def drafts(request):
    # Show drafts saved by the current user.
    queryset = Message.objects.filter(
        sender=request.user,
        status=Message.STATUS_DRAFT,
    ).select_related("sender", "recipient")
    context = _folder_context(
        request.user,
        "drafts",
        "Draft Messages",
        "Pick up unfinished drafts and send them when they are ready.",
        queryset,
    )
    return render(request, "messages_app/message_list.html", context)


@login_required
def new_message(request, message_id=None):
    draft = None
    if message_id is not None:
        # Only the user who made the draft can edit it.
        draft = get_object_or_404(
            Message,
            pk=message_id,
            sender=request.user,
            status=Message.STATUS_DRAFT,
        )

    if request.method == "POST":
        form = MessageForm(request.POST, instance=draft, user=request.user)
        if form.is_valid():
            # Save later so we can set the sender and message status first.
            message_obj = form.save(commit=False)
            message_obj.sender = request.user

            if "send_message" in request.POST:
                # Sending needs full validation, unlike saving a draft.
                if form.validate_for_send():
                    message_obj.mark_as_sent()
                    message_obj.save()
                    messages.success(request, "Message sent successfully.")
                    return redirect("messages_app:detail", pk=message_obj.pk)
            else:
                # Save the work so the user can finish it later.
                message_obj.status = Message.STATUS_DRAFT
                message_obj.save()
                messages.success(request, "Draft saved successfully.")
                return redirect("messages_app:drafts")
    else:
        initial = {}
        # Fill in the recipient automatically when replying.
        recipient_id = request.GET.get("recipient")
        if recipient_id and recipient_id.isdigit():
            initial["recipient"] = recipient_id
        form = MessageForm(instance=draft, user=request.user, initial=initial)

    context = {
        "form": form,
        "draft": draft,
        "page_title": "New Message" if draft is None else "Edit Draft",
        "page_sub": "Write a new message or save it as a draft until you are ready to send it.",
    }
    context.update(_mailbox_counts(request.user))
    return render(request, "messages_app/compose_message.html", context)


@login_required
def message_detail(request, pk):
    # This page shows the full message content.
    message_obj = get_object_or_404(
        Message.objects.select_related("sender", "recipient"),
        pk=pk,
    )

    # Only the sender or recipient should be able to open the message.
    if request.user not in {message_obj.sender, message_obj.recipient}:
        return redirect("messages_app:inbox")

    if (
        message_obj.recipient == request.user
        and message_obj.status == Message.STATUS_SENT
        and not message_obj.is_read
    ):
        # Mark the message as read when the receiver opens it.
        message_obj.is_read = True
        message_obj.save(update_fields=["is_read"])

    context = {
        "message_obj": message_obj,
        "page_title": "Message Detail",
        "page_sub": "Review the full message content and continue the conversation if needed.",
        "can_edit_draft": message_obj.sender == request.user and message_obj.status == Message.STATUS_DRAFT,
        "reply_recipient_id": message_obj.sender_id if message_obj.recipient == request.user else "",
    }
    context.update(_mailbox_counts(request.user))
    return render(request, "messages_app/message_detail.html", context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
