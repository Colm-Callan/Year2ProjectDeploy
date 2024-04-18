from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_loyal = models.BooleanField(default=False, blank=False, null=False)
    address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField(blank=True, null=True)
