import mongoengine

class Expense(mongoengine.Document):
    date = mongoengine.DateTimeField()
    value = mongoengine.FloatField()
    category = mongoengine.StringField()
    comment = mongoengine.StringField()