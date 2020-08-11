from django.test import TestCase, Client
from . models import matchData
import json
from rest_framework import status
from django.urls import reverse
from .serializers import matchDataSerializer

# Create your tests here.


class basicTest(TestCase):

	
	def test_fields(self):
		match=matchData.objects.create(HomeTeam="Arsenal", 
			AwayTeam="Liverpool",
			Referee = "robert",
			AttackRateH	= .02,
			AttackRateA	= .1,
			DefenceRateH = .4,
			DefenceRateA = .5,
			DGH	= .6,
			DGA	= .7,
			HomeRank = .8,
			AwayRank = .9,
			AvgHST	= .10,
			AvgAST	= .11,
			AvgHF	= .22,
			AvgAF	= .33,
			AvgHC	=.44,
			AvgAC	= .55,
			AvgHR	= .66,
			AvgAR	= .77,
			AvgHY	=.99,
			AvgAY =.78 )
		
		record=matchData.objects.get(pk=1)
		self.assertEqual(record,match)






