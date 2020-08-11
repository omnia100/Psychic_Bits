
from django.db import models
from PsychicBits.models import Match
from users.models import Profile

class prediction(models.Model):
	userID=models.ForeignKey(Profile,models.SET_NULL,blank=True,null=True,)
	matchID=models.ForeignKey(Match,models.SET_NULL,blank=True,null=True,)
	vote=models.CharField(max_length=1)



	#def __str__(self):
	#	return self.vote

#	def getUser(self):
#		return userID




