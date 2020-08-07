from django.db import models
from django.contrib.auth.models import User, UserManager


# user: username, email, password
# user optionally has a profile

class Profile(models.Model):
    objects = UserManager
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(blank=True)
    score = models.IntegerField(default=0)

