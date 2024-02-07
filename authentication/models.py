from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)