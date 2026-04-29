from django.db import models


class Meeting(models.Model):
    PLATFORM_CHOICES = [
        ('teams', 'Microsoft Teams'),
        ('zoom', 'Zoom'),
        ('slack', 'Slack'),
        ('google_meet', 'Google Meet'),
        ('in_person', 'In Person'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"