import datetime
import re
from enum import Enum
from src.database.expense_dao import ExpenseDao

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
            return 'Invalid content'
        elif 'Illegal' in str(database_expense_value):
            return 'Invalid content'
        elif 'Illegal' in database_expense_category:
            return 'Invalid content'
        elif 'Illegal' in database_expense_comment:
            return 'Invalid content'

        validated_json = {'value': database_expense_value, 'date': database_expense_date, 
        'category': database_expense_category, 'comment': database_expense_comment}
        print(validated_json)
        return validated_json

    @classmethod
    def insert(cls, json):
        validated_json = cls.json_content_validation(json)
        if validated_json != 'Invalid content':
            ExpenseDao.insert(validated_json)
            return 'All correct, inserted into db'
        else:
            return 'Illegal Json'

    @classmethod
    def remove(cls, json):
        validated_json = cls.json_content_validation(json)
        if validated_json != 'Invalid content':
            ExpenseDao.remove(validated_json)
            return 'All correct, removed from db'
        else:
            return 'Illegal Json'

    @classmethod
    def find(cls):
        return ExpenseDao.find()
