import datetime

from peewee import *

DATABASE = SqliteDatabase('veggiedish.db')

class User(Model):
    full_name = CharField()
    email = CharField()
    password = CharField()
    date_joined = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-datejoined',)

class Recipe(Model):
    name = CharField()
    image = CharField()
    description = TextField()
    ingredients = TextField()
    instructions = TextField()
    average_rating = IntegerField(default=0)

    class Meta:
    database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe], safe=True)
    DATABASE.close()

    