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
    title = models.CharField(max_length=200, default='cash')
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Contribution amount in local currency"
    )
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, default='dues')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.amount}"

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
    first_name = models.CharField(max_length=255)  # New field for first name
    last_name = models.CharField(max_length=255)   # New field for last name
    email = models.EmailField(max_length=254, unique=True)          # Email field
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Phone number field
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)  # Gender field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Update representation
