# Generated by Django 5.1.7 on 2025-04-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baduma_youths', '0012_projects_rename_title_contribution_contribution_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, default='000  00 00 000', max_length=20, null=True),
        ),
    ]
