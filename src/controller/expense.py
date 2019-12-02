from flask_restful import Resource
from flask import request
from . import config

class Expense(Resource):

    def post(self):
        json = request.json
        
        return json