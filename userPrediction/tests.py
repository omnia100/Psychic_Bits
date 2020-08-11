from django.test import TestCase, Client
from django.urls import reverse, resolve
from . views import vote, calculateScore, showPrediction
from django.test import SimpleTestCase
from . models import prediction

#make sure that each function could catch the tru input


class testUrls(SimpleTestCase):

	def test_score_url_resolve(self):
		url =reverse ('score',args=['1','w'])
		self.assertEquals(resolve(url).func, calculateScore)



	def test_vote_url_resolve(self):
		url =reverse ('vote',args=['amira','1','L'])
		self.assertEquals(resolve(url).func, vote)



	def test_showPrediction_url_resolve(self):
		url =reverse ('prediction',args=['1'])
		self.assertEquals(resolve(url).func, showPrediction)






		

