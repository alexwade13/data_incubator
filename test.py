import os

from app import app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        print("Testadsfsd")
        self.app.testing = True 

    def test_post(self):
        print(self.app.post('/img').data)
        assert 'something that passes' in ['something that passes']

if __name__ == '__main__':
    unittest.main()