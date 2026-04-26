from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('teams/', include('teams.urls')),
    path('organisation/', include('organisation.urls')),
    path('messages/', include('messages_app.urls')),
    path('schedule/', include('schedule.urls')),
    path('reports/', include('reports.urls')),
]