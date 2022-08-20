from cuser.models import AbstractCUser
from django.db import models


class User(AbstractCUser):
    pass


class Survey(models.Model):
    data = models.TextField(null=True, blank=True)


class Answer(models.Model):
    data = models.TextField(null=True, blank=True)
