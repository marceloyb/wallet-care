import datetime
import re
from src.database import expense_dao
from enum import Enum

class ExpenseCategory(Enum):

    RESTAURANTE = 'Restaurante'
    MERCADO = 'Mercado'
    LAZER = 'Lazer'
    COMBUSTIVEL = 'Combustivel'
    APP_TRANSPORTE = 'App Transporte'
    EXTRA_CARTAO = 'Extra Cartao'
    PARCELAS_CARTAO = 'Parcelas Cartao'
    ESPORTES = 'Esportes'

class Expense:

    @classmethod
    def date_validation(cls, input_date):
        input_date_format = '%d/%m/%Y'
        database_date_format = '%Y-%m-%d'
        
        # converting from DD/MM/YYYY to YYYY-MM-DD
        try:
            date = datetime.datetime.strptime(input_date, input_date_format).strftime(database_date_format)
            return date            
        except ValueError:
            return 'Illegal date'

    @classmethod
    def value_validation(cls, value):
        if re.search('[^0-9.]', value):
            return 'Illegal value' 
        else:
            return float(value)
    
    @classmethod
    def category_validation(cls, category):
        for enum_category in ExpenseCategory:
            if category == enum_category.value:
                return enum_category.value

        return 'Illegal category'

    @classmethod
    def comment_validation(cls, comment):
        if len(comment) > 20 or re.search('[^a-zA-Z ]', comment):
            return 'Illegal comment' 
        else:
            return comment

    @classmethod
    def json_content_validation(cls, json):
        return_message = 'All correct'
        database_expense_date = cls.date_validation(json['date'])
        database_expense_value = cls.value_validation(json['value'])
        database_expense_category = cls.category_validation(json['category'])
        database_expense_comment = cls.comment_validation(json['comment'])

        if 'Illegal' in str(database_expense_date):
            return_message = 'Invalid content'
        elif 'Illegal' in str(database_expense_value):
            return_message = 'Invalid content'
        elif 'Illegal' in database_expense_category:
            return_message = 'Invalid content'
        elif 'Illegal' in database_expense_comment:
            return_message = 'Invalid content'

        return return_message

    @classmethod
    def insert(cls, json):
        validation = cls.json_content_validation(json)
        if validation == 'All correct':
            expense_dao.insert(json)
            return 'All correct, inserted into db'
        else:
            return 'Illegal Json'