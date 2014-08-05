import unittest
import ex2

class Ex2TestCase(unittest.TestCase):
	def setUp(self):
		self.app = ex2.app.test_client()
		
	def test_name(self):
		rv = self.app.get('/zac')
		assert "<h1>Hello zac!</h1>" in rv.data

if __name__ == '__main__':
	unittest.main()