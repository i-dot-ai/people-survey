from cuser.models import AbstractCUser
from django.db import models


class User(AbstractCUser):
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class Survey(models.Model):
    data = models.TextField(null=True, blank=True)


class Answer(models.Model):
    data = models.TextField(null=True, blank=True)
