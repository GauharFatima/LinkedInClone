from django.db import models
from AccountsApp.models import MyUser


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=100, blank=True)
    profile_pic = models.ImageField(
        upload_to='profilePics/', null=True, blank=True)


class Education(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=255, blank=False)
    degree = models.CharField(max_length=255)
    start_year = models.DateField(help_text='Format: YYYY-MM')
    end_year = models.DateField(
        null=True, blank=True, help_text='Format: YYYY-MM')
    description = models.TextField(max_length=1000)


class Skill(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=255)


class Experience(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    SELF_EMPLOYED = 'SE'
    FREELANCE = 'FE'
    INTERNSHIP = 'IT'
    TRAINEE = 'TE'
    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, 'Full-time'),
        (PART_TIME, 'Part-time'),
        (SELF_EMPLOYED, 'Self-employed'),
        (FREELANCE, 'Freelance'),
        (INTERNSHIP, 'Internship'),
        (TRAINEE, 'Trainee'),
    ]

    ONSITE = 'OS'
    HIBRATE = 'HY'
    REMOTE = 'RE'
    LOCATION_TYPE_CHOICES = [
        (ONSITE, 'On-site'),
        (HIBRATE, 'Remote'),
        (REMOTE, 'Hybrid'),
    ]
    DEFAULT_TYPE = 'Please select'
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='experiences')
    employment_type = models.CharField(
        max_length=2, choices=EMPLOYMENT_TYPE_CHOICES, default=DEFAULT_TYPE)
    company_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    location_type = models.CharField(
        max_length=2, choices=LOCATION_TYPE_CHOICES, default=DEFAULT_TYPE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
