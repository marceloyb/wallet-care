import unittest

from src.controller import config

class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.client = config.app.test_client()
        self.response = self.client.get('/')

    # testing answer code from root page
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    #testing answer string from root page
    def test_html_string_answer(self):
        self.assertEqual("Server talk scheduling up", self.response.data.decode('utf-8'))