from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
