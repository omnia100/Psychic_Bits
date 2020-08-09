from django.db import models
from django.contrib.auth.models import User


# user: username, email, password
# user optionally has a profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # photo = models.ImageField(blank=True)
    photo = models.URLField(default="https://classeventie.classiebit.com//upload/users/images/1537002962360.png")
    #photo = models.URLField(default="static/users/av3.png")
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'