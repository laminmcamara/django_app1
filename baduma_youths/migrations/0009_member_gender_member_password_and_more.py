# Generated by Django 5.1.7 on 2025-03-28 07:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baduma_youths', '0008_alter_contribution_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='current_address',
            field=models.TextField(blank=True, default='The Gambia'),
        ),
    ]
