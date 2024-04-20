from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.username
    
class Userlog(models.Model):
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()