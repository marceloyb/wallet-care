import datetime
import re

class Expense:

    @classmethod
    def date_validation(cls, input_date):
        input_date_format = '%d/%m/%Y'
        database_date_format = '%Y-%m-%d'
        
        try:
            date = datetime.datetime.strptime(input_date, input_date_format).strftime(database_date_format)
            return date            
        except ValueError:
            return 'Date dont match %d/%m/%Y format'

        return date_obj

    @classmethod
    def value_validation(cls, input_value):
        database_input = re.sub('[^0-9.]', '', input_value)

        if not database_input:
            return 'Value input is in bad format' 
        else:
            return float(database_input)

    @classmethod
    def insert(cls, json):
        insert_expense_date = cls.date_validation(json['date'])
        insert_expense_value = cls.value_validation(json['value'])

        return 'All correct, inserted into db'