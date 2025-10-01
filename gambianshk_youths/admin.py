from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Meeting, Attendance, Member,
    Contribution, Project, Event, Constitution,
    Expense, Budget, FinancialReport
)

# --- Site Header Configuration ---
admin.site.site_header = "Gambians based in Hong Kong Administration"
admin.site.site_title = "Gambians based in Hong Kong Admin Portal"
admin.site.index_title = "Welcome to Gambians based in Hong Kong Admin"


@admin.register(Constitution)
class ConstitutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'effective_date', 'last_updated')
    search_fields = ('title', 'content')
    ordering = ['title'] 


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone_number',
        'gender', 'marital_status', 'joined_date'
    )
    list_filter = ('gender', 'marital_status', 'career')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'career')
    ordering = ('last_name', 'first_name')


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'location', 'agenda')
    ordering = ('-date',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'meeting', 'date_recorded')  
    list_filter = ('meeting', 'date_recorded')
    search_fields = ('member__first_name', 'member__last_name', 'meeting__title')
    autocomplete_fields = ('member', 'meeting')  
    date_hierarchy = 'date_recorded'


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = (
        'member', 'contribution_type', 'amount', 'date', 'verified', 'published'
    )
    list_filter = ('contribution_type', 'verified', 'published', 'date')
    search_fields = ('member__first_name', 'member__last_name', 'description')
    date_hierarchy = 'date'
    ordering = ('-date',)
    autocomplete_fields = ('member',)  


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'amount', 'date', 'approved', 'incurred_by')
    list_filter = ('category', 'approved', 'date')
    search_fields = ('description', 'notes', 'incurred_by__first_name', 'incurred_by__last_name')
    date_hierarchy = 'date'
    ordering = ('-date',)
    autocomplete_fields = ('incurred_by',)  


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('year', 'total_income', 'total_expenses', 'balance', 'updated_at')
    search_fields = ('year', 'notes')
    ordering = ('-year',)


@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('budget', 'generated_on', 'summary')  
    search_fields = ('budget__year', 'summary')
    date_hierarchy = 'generated_on'
    ordering = ('-generated_on',)
    autocomplete_fields = ('budget',)  


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'start_date', 'end_date', 'created_at', 'display_image', 'display_video', 'display_audio')
    ordering = ('start_date',)

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Description'

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return 'No Image'
    display_image.short_description = 'Image'

    def display_video(self, obj):
        if obj.video:
            return format_html('<a href="{}" target="_blank">View Video</a>', obj.video.url)
        return 'No Video'
    display_video.short_description = 'Video'

    def display_audio(self, obj):
        if obj.audio:
            return format_html('<a href="{}" target="_blank">Listen Audio</a>', obj.audio.url)
        return 'No Audio'
    display_audio.short_description = 'Audio'

admin.site.register(Project, ProjectAdmin)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'start_date', 'end_date', 'location')  # Ensure these fields exist
    list_filter = ('start_date', 'location')  # Ensure these fields exist
    search_fields = ('title', 'description', 'location')
    ordering = ('-start_date',)
    
    def image_tag(self, obj):
        # The 'if obj.image' check prevents an error if no image has been uploaded
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 150px; height:auto;" />')
        return ""
    
    image_tag.short_description = 'Event Image' 
    

# NOTE: CMSPlugin models (MemberPlugin, ContributionPlugin) are managed via the
# frontend editing interface of django CMS and are typically not registered here.
