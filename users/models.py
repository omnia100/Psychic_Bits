from django.db import models
from django.contrib.auth.models import User


# user: username, email, password
# user optionally has a profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # photo = models.ImageField(blank=True)
    photo = models.URLField(default="https://robohash.org/suscipitnequeut.png?size=170x170&set=set1")
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'