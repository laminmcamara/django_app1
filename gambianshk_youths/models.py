# gambianshk_youths/models.py

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.contrib.auth.models import User  # Import User model

# from cms.models.pluginmodel import CMSPlugin
from cms.models import CMSPlugin  # Assuming you're using Django CMS


# --- CORRECTED IMPORTS ---
# We will only use CKEditor5Field from the new package.
from django_ckeditor_5.fields import CKEditor5Field

# We are removing these unused or outdated imports:
# from djangocms_text_ckeditor.fields import HTMLField
# from ckeditor.fields import RichTextField


# Define the Constitution model
class Constitution(CMSPlugin):
    title = models.CharField(max_length=200)
    # BEFORE: content = RichTextField(blank=True)
    content = CKEditor5Field(blank=True, config_name='default')
    effective_date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Define the Member model
class Member(CMSPlugin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member', default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    marital_status = models.CharField(max_length=20, choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed')], blank=True)
    career = models.CharField(max_length=100, blank=True)
    # BEFORE: educational_background = RichTextField(blank=True)
    educational_background = CKEditor5Field(blank=True, config_name='default')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the Contribution model
class Contribution(CMSPlugin):
    CONTRIBUTION_TYPES = [
        ('Donation', 'Donation'),
        ('Membership Fee', 'Membership Fee'),
        ('Sponsorship', 'Sponsorship'),
        ('Monthly Contribution', 'Monthly Contribution'),
        ('Other', 'Other'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    contribution_type = models.CharField(max_length=50, choices=CONTRIBUTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(default=timezone.now)
    verified = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    # BEFORE: description = RichTextField(blank=True)
    description = CKEditor5Field(blank=True, config_name='default')

    def __str__(self):
        return f"Contribution from {self.member} - {self.contribution_type} ({self.amount})"

# Define the Expense model
class Expense(CMSPlugin):
    CATEGORY_CHOICES = [
        ('Operations', 'Operations'),
        ('Events', 'Events'),
        ('Administration', 'Administration'),
        ('Projects', 'Projects'),
        ('Other', 'Other'),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    # BEFORE: description = RichTextField(blank=True)
    description = CKEditor5Field(blank=True, config_name='default')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(default=timezone.now)
    incurred_by = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    approved = models.BooleanField(default=False)
    receipt = models.FileField(upload_to='expenses/receipts/', blank=True, null=True)
    # BEFORE: notes = RichTextField(blank=True)
    notes = CKEditor5Field(blank=True, config_name='default')

    def __str__(self):
        return f"{self.category} expense of {self.amount} on {self.date}"

# Define the Budget model
class Budget(CMSPlugin):
    year = models.PositiveIntegerField(unique=True)
    total_income = models.DecimalField(max_digits=14, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # BEFORE: notes = RichTextField(blank=True)
    notes = CKEditor5Field(blank=True, config_name='default')

    @property
    def balance(self):
        return self.total_income - self.total_expenses

    def __str__(self):
        return f"Budget for {self.year}"

# Define the FinancialReport model
class FinancialReport(CMSPlugin):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    generated_on = models.DateTimeField(auto_now_add=True)
    # BEFORE: summary = RichTextField(blank=True)
    summary = CKEditor5Field(blank=True, config_name='default')
    report_file = models.FileField(upload_to='financial_reports/', blank=True, null=True)

    def __str__(self):
        return f"Financial Report for {self.budget} generated on {self.generated_on.date()}"

class Event(CMSPlugin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Optional. Leave blank for single-day events."
    )
    # BEFORE: description = RichTextField(...)
    description = CKEditor5Field(
        blank=True,
        help_text="Full details of the event. Use the text editor to format content.",
        config_name='default'
    )
    location = models.CharField(max_length=255, blank=True, verbose_name=("Location"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='event_image',
        help_text="A promotional image for the event."
    )
    video_url = models.URLField(
        blank=True,
        help_text="Optional. A URL to a video on a platform like YouTube or Vimeo."
    )
    video_file = FilerFileField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='event_video_file',
        help_text="Optional. Upload a video file directly (e.g., MP4)."
    )
    audio_file = FilerFileField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='event_audio_file',
        help_text="Optional. Upload an audio file (e.g., MP3)."
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ['-start_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})

# Define the Meeting model
class Meeting(CMSPlugin):
    title = models.CharField(max_length=255, verbose_name=_("Meeting Title"))
    date = models.DateTimeField(verbose_name=_("Meeting Date"))
    # BEFORE: agenda = RichTextField(...)
    agenda = CKEditor5Field(blank=True, verbose_name=_("Agenda"), config_name='default')
    # BEFORE: minutes = RichTextField(...)
    minutes = CKEditor5Field(blank=True, verbose_name=_("Minutes"), config_name='default')
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Location"))
    image = models.ImageField(upload_to='meeting_images/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Meeting")
        verbose_name_plural = _("Meetings")
        ordering = ['-date', 'title']

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d %H:%M')}"

# Define the Attendance model
class Attendance(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='attendance_images/')
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attendance: {self.member} at {self.meeting}"

    class Meta:
        unique_together = ('meeting', 'member')

class ImageFlexbox(CMSPlugin):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

class Project(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    video = models.FileField(upload_to='project_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='project_audios/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    # This model was already correct
    content = CKEditor5Field('Content', blank=True, null=True, config_name='default')