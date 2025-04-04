from django.contrib import admin
from .models import Member, Contribution, Community, Event, CMSContent

# MemberAdminPanel
class MemberAdminPanel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'gender']  # Updated fields
    list_filter = ['email', 'gender']  # Filter by email and gender
    search_fields = ['first_name', 'last_name', 'email']  # Enable search by first name, last name, or email

# ContributionAdminPanel
class ContributionAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date', 'verified']  # Fields from the Contribution model
    list_filter = ['verified', 'date']  # Filter by verification status and date
    list_editable = ['verified']  # Allow editing the 'verified' field directly in the admin list view
    search_fields = ['title', 'description']  # Enable search by title or description

# CommunityAdminPanel
class CommunityAdminPanel(admin.ModelAdmin):
    list_display = ['name', 'description']  # Fields from the Community model
    search_fields = ['name']  # Enable search by name

# EventAdminPanel
class EventAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'date', 'community']  # Fields from the Event model
    list_filter = ['date', 'community']  # Filter by date and community
    search_fields = ['title']  # Enable search by title

# CMSContentAdminPanel
class CMSContentAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date']  # Fields from the CMSContent model
    list_filter = ['date']  # Filter by date
    search_fields = ['title']  # Enable search by title

# Register models with their respective admin classes
admin.site.register(Member, MemberAdminPanel)
admin.site.register(Contribution, ContributionAdminPanel)
admin.site.register(Community, CommunityAdminPanel)
admin.site.register(Event, EventAdminPanel)
admin.site.register(CMSContent, CMSContentAdminPanel)