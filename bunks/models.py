from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    photo = models.CharField(max_length=200, default="https://pbs.twimg.com/profile_images/3403341918/71c895ce6b9f016a0381eadfa2738f27_400x400.png")

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user_set")
    to_user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user_set")
    time = models.DateTimeField('date', auto_now_add=True)