from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=50, null=True)
    user_profile_loc = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects=CustomUserManager()
 
    def __str__(self):
        return self.email