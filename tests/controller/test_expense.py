import unittest

from src.controller import *

class ConfigTest(unittest.TestCase):
    def set_up(self):
        self.client = config.app.test_client()

    def test_html_string_answer(self):
        json_request = {'value': '5', 'date': '12/11/2019'}

        response = self.client.post('/api/expense', json=json_request)

        json_response = response.json
        self.assertEqual('5', json_response['value'])
        self.assertEqual('12/11/2019', json_response['date'])