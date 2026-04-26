from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
<<<<<<< HEAD
=======
    path('', views.reports_index, name='index'),
    path('departments/', views.department_summary, name='department_summary'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export/excel/', views.export_excel, name='export_excel'),
>>>>>>> 8289812d87f73ee31ade840543d36b3bee9ca8e6
]