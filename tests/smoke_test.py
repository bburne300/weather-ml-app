import unittest
from app import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestAppSmoke(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
	
	# Complete the function below to test a success in running the application
	def test_prediction_route_success(self):
		response = self.client.get('/')
		# assertion - check if the status is 200 meaning ok
		self.assertEqual(response.status_code, 200, "Main page did not load successfully")

	# Complete the function below to test a form is rendered
	def test_get_form(self):
		response = self.client.get('/')
		# assertion - check the respone uses a <form> tag
		self.assertIn(b'<form', response.data, "Form tag not found in response")

if __name__ == '__main__':
	unittest.main()
