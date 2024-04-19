from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.username