from django.test import TestCase
from . models import Match

# Create your tests here.
"""

class basicTest(TestCase):

	def test_fields(self):
		m=Match.objects.create( 
		date = '10-25-06',
		HT = 'Arsenal',
		AT = 'Liverpool',
		pred = 'w',
		FTR = 'w').save()

	record=Match.objects.get(pk=1)
	self.assertEqual(record,m)

		
	
"""