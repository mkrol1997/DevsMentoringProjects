from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_failed_login = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'Profile of {self.user.username}'
