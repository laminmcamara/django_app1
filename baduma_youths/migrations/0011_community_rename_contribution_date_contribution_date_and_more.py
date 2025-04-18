# Generated by Django 5.1.7 on 2025-04-04 15:03

import cms.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baduma_youths', '0010_auto_20250403_1622'),
        ('cms', '0037_alter_cmsplugin_id_alter_globalpagepermission_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='contribution',
            old_name='contribution_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='contribution',
            name='contribution_type',
        ),
        migrations.RemoveField(
            model_name='member',
            name='age',
        ),
        migrations.RemoveField(
            model_name='member',
            name='current_address',
        ),
        migrations.RemoveField(
            model_name='member',
            name='education',
        ),
        migrations.RemoveField(
            model_name='member',
            name='join_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.RemoveField(
            model_name='member',
            name='position',
        ),
        migrations.AddField(
            model_name='contribution',
            name='description',
            field=models.TextField(blank=True, default='dues'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='title',
            field=models.CharField(default='cash', max_length=200),
        ),
        migrations.AddField(
            model_name='contribution',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='amount',
            field=models.DecimalField(decimal_places=2, help_text='Contribution amount in local currency', max_digits=10),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='baduma_youths.member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='CMSContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('custom_placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='custom_placeholder', to='cms.placeholder')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baduma_youths.community')),
            ],
        ),
    ]
