from django.urls import path
from . import views

urlpatterns = [
    path("", views.schedule_home, name="schedule_home"),
    path("create/", views.create_meeting, name="create_meeting"),
    path("delete/<int:meeting_id>/", views.delete_meeting, name="delete_meeting"),
]