
from django.db import models
from PsychicBits.models import Match

# Create your models here.

class prediction(models.Model):
	#userID=models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)
	matchID=models.ForeignKey(Match,models.SET_NULL,blank=True,null=True,)
	vote=models.CharField(max_length=5)



	def __str__(self):
		return self.vote

