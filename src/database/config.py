from mongoengine import connect
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/wallet-care')
db = client.wallet_care
# for db in client.list_databases():
#     print(db)
# for collection in db():
#     print (collection)
data = db.expense.find().count()
print (data)

# print(db.expense.find_one())

# collection = db.expense
# collection.find_one()