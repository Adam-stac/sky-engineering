<<<<<<< HEAD
# Name: Ayaan Surani
# Student ID: W2070551
# Student: Student 3
# Feature: Messages
# Contribution: Individual work to make message records visible in Django admin.

from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # This makes messages easier to manage in Django admin.
    list_display = ("subject", "sender", "recipient", "status", "is_read", "sent_at", "updated_at")
    list_filter = ("status", "is_read", "sent_at")
    search_fields = ("subject", "body", "sender__username", "recipient__username")

=======
from django.contrib import admin

# Register your models here.
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
