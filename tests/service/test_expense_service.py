import unittest
import datetime
from src.service import *


class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.service = expense_service.Expense()

    def test_date_validation_positive(self):
        expected_value = '2019-11-12'
        test_input = '12/11/2019'

        value = self.service.date_validation(test_input)

        self.assertEqual(expected_value, value)

    def test_date_validation_negative(self):
        expected_value = 'Date dont match %d/%m/%Y format'
        test_input = '12/27/2019'

        value = self.service.date_validation(test_input)

        self.assertEqual(expected_value, value)
    
    def test_value_validation_positive(self):
        expected_value = 5.0
        test_input = '5.0'

        value = self.service.value_validation(test_input)

        self.assertEqual(expected_value, value)
    
    def test_value_validation_negative(self):
        expected_value = 'Value input is in bad format'
        test_input = 'cmd injection'

        value = self.service.value_validation(test_input)

        self.assertEqual(expected_value, value)

# Enum categories validation

    def test_category_validation_positive(self):
        expected_value = 'Restaurante'

        self.assertEqual('Restaurante', expected_value)

    def test_create_new_expense(self):
        expected_value = 'All correct, inserted into db'
        test_json_input = {'value': '5', 'date': '12/11/2019'}

        value = self.service.insert(test_json_input)

        self.assertEqual(expected_value, value)