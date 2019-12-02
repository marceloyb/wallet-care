from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/wallet-care')
db = client.wallet_care

# descobrir como dar import nas configs do banco

def insert(json):
    db.expense.insert_one(json)