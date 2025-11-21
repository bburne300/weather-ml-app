import unittest
from app import app

class TestAppSmoke(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
	
	# Complete the function below to test a success in running the application
	def test_prediction_route_success(self):
		response = self.client.get('/')
		

	# Complete the function below to test a form is rendered
	def test_get_form(self):
		response = self.client.get('/')
		
 
if __name__ == '__main__':
	unittest.main()
