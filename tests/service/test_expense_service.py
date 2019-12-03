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
        expected_value = 'Illegal date'
        test_input = '12/27/2019'

        value = self.service.date_validation(test_input)

        self.assertEqual(expected_value, value)
    
    def test_value_validation_positive(self):
        expected_value = 5.0
        test_input = '5.0'

        value = self.service.value_validation(test_input)

        self.assertEqual(expected_value, value)
    
    def test_value_validation_negative(self):
        expected_value = 'Illegal value'
        test_input = 'cat /etc/passwd'

        value = self.service.value_validation(test_input)

        self.assertEqual(expected_value, value)

    def test_category_validation_positive(self):
        expected_value = 'Mercado'
        test_input = 'Mercado'

        value = self.service.category_validation(test_input)

        self.assertEqual(expected_value, value)

    def test_category_validation_negative(self):
        expected_value = 'Illegal category'
        test_input = 'Balada'

        value = self.service.category_validation(test_input)

        self.assertEqual(expected_value, value)

    def test_comment_validation_positive(self):
        expected_value = 'Sabores do Lar'
        test_input = 'Sabores do Lar'

        value = self.service.comment_validation(test_input)

        self.assertEqual(expected_value, value)

    def test_comment_validation_overflow(self):
        expected_value = 'Illegal comment'
        test_input = 'comentario beeem longo'

        value = self.service.comment_validation(test_input)

        self.assertEqual(expected_value, value)

    def test_comment_validation_illegal_char(self):
        expected_value = 'Illegal comment'
        test_input = 'cat /etc/passwd'

        value = self.service.comment_validation(test_input)

        self.assertEqual(expected_value, value)


    def test_validate_full_json_positive(self):
        expected_value = {'value': 19.9, 'date': '2019-11-12', 
        'category': 'Restaurante', 'comment': 'Sabores do Lar'}

        test_json_input = {'value': '19.90', 'date': '12/11/2019', 
        'category': 'Restaurante', 'comment': 'Sabores do Lar'}

        value = self.service.json_content_validation(test_json_input)

        self.assertEqual(expected_value, value)

    def test_validate_full_json_negative(self):
        expected_value = 'Invalid content'
        test_json_input = {'value': '19.90', 'date': '12/11/2019', 
        'category': 'Balada', 'comment': 'Sabores do Lar'}

        value = self.service.json_content_validation(test_json_input)

        self.assertEqual(expected_value, value)


    def test_create_new_expense(self):
        expected_value = 'All correct, inserted into db'
        test_json_input = {'value': '19.90', 'date': '12/11/2019', 
        'category': 'Restaurante', 'comment': 'Sabores do Lar'}

        value = self.service.insert(test_json_input)

        self.assertEqual(expected_value, value)

    def test_find_expenses(self):
        not_expected_value = None

        value = self.service.find()

        self.assertNotEqual(not_expected_value, value)

    def test_remove_expense(self):
        expected_value = 'All correct, removed from db'
        test_json_input = {'value': '19.90', 'date': '12/11/2019', 
        'category': 'Restaurante', 'comment': 'Sabores do Lar'}

        value = self.service.remove(test_json_input)

        self.assertEqual(expected_value, value)