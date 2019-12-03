from pymongo import MongoClient
from mongoengine import connect
from src.database.expense import Expense as Model

client = MongoClient('mongodb://127.0.0.1:27017/wallet-care')
db = client.wallet_care
collection = db.expense
connect('wallet_care')

class ExpenseDao():

    def insert(json):
        entity = Model()
        entity.value = json['value']
        entity.date = json['date']
        entity.category = json['category']
        entity.comment = json['comment']
        result = entity.save()

    def remove(json):
        entity = Model()
        entity.value = json['value']
        entity.date = json['date']
        entity.category = json['category']
        entity.comment = json['comment']
        
        Model.objects(value=entity.value, date=entity.date,
        category=entity.category).first().delete()


    def find():
        entity = Model()

        return Model.objects()
