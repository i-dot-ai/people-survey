from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Answer(models.Model):
    user = models.ForeignKey(User, related_name="answers", on_delete=models.PROTECT)
