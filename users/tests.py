from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve

from django.test import SimpleTestCase





class testUser(TestCase):
	def test_user_login(self):
		
		c = Client()
		user=c.post('/login/', {'name': 'fred', 'passwd': 'secret'})
		c.login(username='fred', password='secret')




	def test_user_logout(self):
		
		c = Client()
		c.post('/logout/')
		
