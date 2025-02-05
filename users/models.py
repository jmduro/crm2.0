from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
