from django.db import models
from django.contrib.auth import get_user_model
from cms.models import PlaceholderField
from django.db import migrations
import uuid
from django.utils import timezone

# Generate UUIDs for existing members
def generate_uuids(apps, schema_editor):
    Member = apps.get_model('baduma_youths', 'Member')
    for member in Member.objects.all():
        member.new_uuid = uuid.uuid4()  # Correct usage of uuid.uuid4()
        member.save()

class Migration(migrations.Migration):
    dependencies = [
        ('baduma_youths', '0004_member_new_uuid'),  # Replace with the previous migration name
    ]

    operations = [
        migrations.RunPython(generate_uuids),
    ]

User = get_user_model()

# Community Model
class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name

# Contribution Model
class Contribution(models.Model):
    member = models.ForeignKey(
        'Member', 
        on_delete=models.CASCADE,
        related_name='contributions'
    )
    contribution_type = models.CharField(max_length=200, default='cash')
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Contribution amount in local currency"
    )
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, default='dues')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.contribution_type} - {self.amount}"

# CMS Content Model
class CMSContent(models.Model):
    custom_placeholder = PlaceholderField('custom_placeholder')
    title = models.CharField(max_length=200)  # Title field for CMS content
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        blank=True, 
        null=True,
        default=0.00
    )  # Amount field for additional information
    date = models.DateField(auto_now_add=True)  # Date field for ordering

    class Meta: 
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.amount}"

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Member Model
class Member(models.Model):
    id = models.AutoField(primary_key=True)  # Default primary key
    new_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='your_first_name')  # New field for first name
    last_name = models.CharField(max_length=255, default='your_last_name')   # New field for last name
    email = models.EmailField(max_length=254, unique=True, default='example@email.com')  # Email field
    phone_number = models.CharField(max_length=20, blank=True, null=True, default='000  00 00 000')  # Phone number field
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, default='male')  # Gender field
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    career = models.CharField(max_length=100, null=True, blank=True, default='civil servant')
    educational_background = models.TextField(null=True, blank=True, default='High school')
    age = models.PositiveIntegerField(null=True, blank=True, default='18')
    marital_status = models.CharField(max_length=10, choices=[('single', 'Single'), ('married', 'Married')], null=True, blank=True, default='single')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Projects Model
class Projects(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    media = models.FileField(upload_to='media/')
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.name

    # Custom method to display additional information
    def short_description(self):
        return self.description[:50]  # Returns the first 50 characters