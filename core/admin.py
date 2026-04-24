from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Engineer, Manager, Department,
    EngineeringTeam, TeamStaffAllocation,
    Dependency, CodeRepository, ContactChannel, AuditLog
)
from .models import (
    User, Engineer, Manager, Department,
    EngineeringTeam, TeamStaffAllocation,
    Dependency, CodeRepository, ContactChannel, AuditLog, TeamType
)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone_number')}),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'leader', 'location', 'created_date')
    search_fields = ('department_name',)

@admin.register(EngineeringTeam)
class EngineeringTeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'department', 'manager', 'status')
    list_filter = ('status', 'department')
    search_fields = ('team_name',)

@admin.register(TeamStaffAllocation)
class TeamStaffAllocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role_in_team', 'date_assigned')

@admin.register(Dependency)
class DependencyAdmin(admin.ModelAdmin):
    list_display = ('source_team', 'target_team', 'criticality_level')

@admin.register(CodeRepository)
class CodeRepositoryAdmin(admin.ModelAdmin):
    list_display = ('repository_name', 'team', 'primary_language', 'is_active')

@admin.register(ContactChannel)
class ContactChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name', 'channel_type', 'team', 'is_active')

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'entity_type', 'user', 'timestamp')
    list_filter = ('action_type',)

@admin.register(TeamType)
class TeamTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date')
    search_fields = ('name',)

admin.site.register(Engineer)
admin.site.register(Manager)