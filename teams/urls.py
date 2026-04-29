from django.urls import path
from . import views

# Name:
# Student ID:
# Student: Student 1
# Feature: Team page routing

app_name = 'teams'

urlpatterns = [
    path("", views.team_list, name="list"),
]
