from django.db import models

# Create your models here.

class matchData(models.Model):
	HomeTeam = models.CharField(max_length=20)
	AwayTeam = models.CharField(max_length=20)
	Referee =  models.CharField(max_length=20)
	AttackRateH	= models.FloatField()
	AttackRateA	= models.FloatField()
	DefenceRateH = models.FloatField()
	DefenceRateA = models.FloatField()
	DGH	= models.FloatField()
	DGA	= models.FloatField()
	HomeRank = models.FloatField()
	AwayRank = models.FloatField()
	AvgHST	= models.FloatField()
	AvgAST	= models.FloatField()
	AvgHF	= models.FloatField()
	AvgAF	= models.FloatField()
	AvgHC	= models.FloatField()
	AvgAC	= models.FloatField()
	AvgHR	= models.FloatField()
	AvgAR	= models.FloatField()
	AvgHY	= models.FloatField()
	AvgAY = models.FloatField()


	def __str__(self):

		return self.HomeTeam 




