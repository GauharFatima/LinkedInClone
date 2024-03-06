from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from AccountsApp.models import MyUser


@receiver(post_save, sender=MyUser)
def create_And_Update_User_Profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
