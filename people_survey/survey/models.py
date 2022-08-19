from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Survey(models.Model):
    data = models.TextField(null=True, blank=True)


class Answer(models.Model):
    data = models.TextField(null=True, blank=True)
