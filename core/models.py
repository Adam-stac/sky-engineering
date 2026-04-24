from django.db import models
from django.contrib.auth.models import AbstractUser


# ============================================================
# CUSTOM USER
# ============================================================
class User(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    ]
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')

    def __str__(self):
        return f"{self.username} ({self.role})"

# ISA SUBTYPES

class Engineer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    technical_level = models.CharField(max_length=100, blank=True)
    specialisation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - Engineer"


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    management_level = models.CharField(max_length=100, blank=True)
    reports_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Manager"

# DEPARTMENT

class Department(models.Model):
    department_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    leader = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='led_departments'
    )
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

# TEAM TYPE

class TeamType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name    

# ENGINEERING TEAM

class EngineeringTeam(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('restructuring', 'Restructuring'),
        ('disbanded', 'Disbanded'),
    ]
    team_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    purpose = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    slack_channel = models.CharField(max_length=200, blank=True)
    teams_channel = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_teams'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        related_name='teams'
    )
    team_type = models.ForeignKey(
    'TeamType',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='teams'
    )

    def __str__(self):
        return self.team_name

# TEAM MEMBERSHIP

class TeamStaffAllocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allocations')
    team = models.ForeignKey(EngineeringTeam, on_delete=models.CASCADE, related_name='members')
    date_assigned = models.DateField(auto_now_add=True)
    role_in_team = models.CharField(max_length=100, default='member')

    class Meta:
        unique_together = ('user', 'team')

    def __str__(self):
        return f"{self.user.username} in {self.team.team_name}"

# DEPENDENCIES (upstream / downstream)

class Dependency(models.Model):
    CRITICALITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    source_team = models.ForeignKey(
        EngineeringTeam,
        on_delete=models.CASCADE,
        related_name='upstream_dependencies'
    )
    target_team = models.ForeignKey(
        EngineeringTeam,
        on_delete=models.CASCADE,
        related_name='downstream_dependencies'
    )
    dependency_type = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    criticality_level = models.CharField(max_length=20, choices=CRITICALITY_CHOICES, blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('source_team', 'target_team')

    def __str__(self):
        return f"{self.source_team} → {self.target_team}"

# CODE REPOSITORY

class CodeRepository(models.Model):
    repository_name = models.CharField(max_length=200)
    repository_url = models.URLField(unique=True)
    repository_type = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    primary_language = models.CharField(max_length=100, blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    team = models.ForeignKey(
        EngineeringTeam,
        on_delete=models.CASCADE,
        related_name='repositories'
    )

    def __str__(self):
        return self.repository_name

# CONTACT CHANNEL

class ContactChannel(models.Model):
    CHANNEL_TYPES = [
        ('slack', 'Slack'),
        ('teams', 'Teams'),
        ('email', 'Email'),
        ('other', 'Other'),
    ]
    channel_type = models.CharField(max_length=20, choices=CHANNEL_TYPES)
    channel_name = models.CharField(max_length=200)
    channel_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    team = models.ForeignKey(
        EngineeringTeam,
        on_delete=models.CASCADE,
        related_name='contact_channels'
    )

    def __str__(self):
        return f"{self.channel_type} - {self.channel_name}"

# AUDIT LOG

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(EngineeringTeam, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    entity_type = models.CharField(max_length=100)
    entity_id = models.IntegerField()
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.action_type} on {self.entity_type} at {self.timestamp}"