from mongoengine import connect
from pymongo import MongoClient

MongoClient("mongodb://127.0.0.1:27017/wallet-care")
connect('wallet-care')