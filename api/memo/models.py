from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=30, null=True)
    bio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username

# Create your models here.