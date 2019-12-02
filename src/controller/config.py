from flask import Flask
from flask_restful import Api
from flask import request
from . import expense

app = Flask('wallet-care')
api = Api(app)

@app.route('/')
def index():
    return "Server talk scheduling up"

def expense_service_resource_add():
    api.add_resource(expense.Expense, '/api/expense')

def service_start(arguments):
    if arguments['expense']:
        expense_service()