from pymongo import MongoClient
from mongoengine import connect
from expense import Expense as Model

class ExpenseDao():

    client = MongoClient('mongodb://127.0.0.1:27017/wallet-care')
    db = client.wallet_care
    collection = db.expense
    connect('wallet_care')

    def insert(json):
        entity = Model()
        entity.value = json['value']
        entity.date = json['date']
        entity.category = json['category']
        entity.comment = json['comment']
        result = entity.save()
        return {'id': str(result.id), 'category': result.category}

    def remove(json):
        db.expense.delete_one(json)

    def find():
        return db.expense.find()
