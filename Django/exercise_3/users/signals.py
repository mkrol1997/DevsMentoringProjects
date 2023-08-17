from .models import Profile
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_login_failed
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance).save()


@receiver(user_login_failed)
def update_recent_user_failed_login_date(sender, credentials, **kwargs) -> None:
    username = credentials['username']
    user = User.objects.filter(username=username).first()

    if user:
        user.profile.last_failed_login = datetime.today()
        user.profile.save()
