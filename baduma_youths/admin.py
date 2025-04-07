from django.contrib import admin
from .models import Member, Contribution, Community, Event, CMSContent, Projects
from django.utils.translation import gettext_lazy as _

# MemberAdminPanel
class MemberAdminPanel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'gender']
    list_filter = ['gender']  # Filter by gender
    search_fields = ['first_name', 'last_name', 'email']

# ContributionAdminPanel
class ContributionAdminPanel(admin.ModelAdmin):
    list_display = ['member', 'contribution_type', 'amount', 'date', 'verified']
    list_filter = ['verified', 'date', 'member']  # Added member to filter
    list_editable = ['verified']
    search_fields = ['contribution_type', 'description']

# CommunityAdminPanel
class CommunityAdminPanel(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

# EventAdminPanel
class EventAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'date', 'community']
    list_filter = ['date', 'community']
    search_fields = ['title']

# CMSContentAdminPanel
class CMSContentAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date']
    list_filter = ['date']
    search_fields = ['title']

# ProjectsAdminPanel
class ProjectsAdminPanel(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'short_description', 'status']
    search_fields = ['name']
    list_filter = ['status']

# Register models with their respective admin classes
admin.site.register(Member, MemberAdminPanel)
admin.site.register(Contribution, ContributionAdminPanel)
admin.site.register(Community, CommunityAdminPanel)
admin.site.register(Event, EventAdminPanel)
admin.site.register(CMSContent, CMSContentAdminPanel)
admin.site.register(Projects, ProjectsAdminPanel)

# Customize the admin site header and titles
admin.site.site_header = _('Baduma Administration')
admin.site.site_title = _('Admin Site')
admin.site.index_title = _('Welcome to Baduma Admin')