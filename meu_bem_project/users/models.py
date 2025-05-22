from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    def __str__(self):
        return self.username
