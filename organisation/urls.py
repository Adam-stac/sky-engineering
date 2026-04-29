from django.urls import path
from . import views

app_name = 'organisation'

urlpatterns = [
    path('', views.org_home, name='org_home'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('team-types/', views.team_type_list, name='team_type_list'),
    path('dependencies/', views.dependency_list, name='dependency_list'),
    path('org-chart/', views.org_chart, name='org_chart'),
]