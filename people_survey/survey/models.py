from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    objects = BaseUserManager()

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class Survey(models.Model):
    data = models.TextField(null=True, blank=True)


class Answer(models.Model):
    data = models.TextField(null=True, blank=True)
