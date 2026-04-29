# Name: Adam
# Student ID: W2039612
# Student: Student 2
# Feature: Organisation - Department list, Department detail, Dependencies, Org Chart, Team Types

from django.urls import path
from . import views

app_name = 'organisation'

# URL routes for the organisation app.
# Uses app_name namespace so URLs can be referenced as organisation:view_name throughout the project.
urlpatterns = [
    path('', views.org_home, name='org_home'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('team-types/', views.team_type_list, name='team_type_list'),
    path('dependencies/', views.dependency_list, name='dependency_list'),
    path('org-chart/', views.org_chart, name='org_chart'),
]