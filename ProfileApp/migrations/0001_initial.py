# Generated by Django 5.0.2 on 2024-03-02 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AccountsApp', '0003_remove_myuser_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AccountsApp.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_type', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('SE', 'Self-employed'), ('FE', 'Freelance'), ('IT', 'Internship'), ('TE', 'Trainee')], default='Please select', max_length=2)),
                ('company_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('location_type', models.CharField(choices=[('OS', 'On-site'), ('HY', 'Remote'), ('RE', 'Hybrid')], default='Please select', max_length=2)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='ProfileApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('start_year', models.DateField(help_text='Format: YYYY-MM')),
                ('end_year', models.DateField(blank=True, help_text='Format: YYYY-MM', null=True)),
                ('description', models.TextField(max_length=1000)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='ProfileApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='ProfileApp.profile')),
            ],
        ),
    ]
