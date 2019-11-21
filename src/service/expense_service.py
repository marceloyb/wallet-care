import datetime
import re
from enum import Enum

class ExpenseCategory(Enum):

    RESTAURANTE = 'Restaurante'
    MERCADO = 'Mercado'
    LAZER = 'Lazer'
    COMBUSTIVEL = 'Combustivel'
    APP_TRANSPORTE = 'App Transporte'
    EXTRA_CARTAO = 'Extra Cartao'
    PARCELAS_CARTAO = 'Parcelas Cartao'
    MUAY = 'Muay Thai'

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
            return 'Date dont match %d/%m/%Y format'

    @classmethod
    def value_validation(cls, value):
        if re.search('[^0-9.]', value):
            return 'Value input is in bad format' 
        else:
            return float(value)
    
    @classmethod
    def category_validation(cls, category):
        for enum_category in ExpenseCategory:
            if category == enum_category.value:
                return enum_category.value

        return 'Invalid category'

    @classmethod
    def comment_validation(cls, comment):
        if len(comment) > 20:
            return 'Comment cant be larger than 20 chars' 
        elif re.search('[^a-zA-Z ]', comment):
            return 'Comment contains illegal chars'
        else:
            return comment

    @classmethod
    def insert(cls, json):
        database_expense_date = cls.date_validation(json['date'])
        database_expense_value = cls.value_validation(json['value'])
        database_expense_category = cls.category_validation(json['category'])
        database_expense_comment = cls.comment_validation(json['comment'])

        return 'All correct, inserted into db'