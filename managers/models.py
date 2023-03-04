from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.





class managersm(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(blank=True, unique=True)

    REQUIRED_FIELDS = ['username']

