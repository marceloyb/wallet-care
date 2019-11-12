from flask import Flask
from flask_restful import Api
from flask import request

app = Flask('wallet-care')
api = Api(app)


@app.route('/')
def index():
    return "Server talk scheduling up"