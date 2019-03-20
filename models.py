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
        order_by = ('-date_joined',)

class Recipe(Model):
    name = CharField()
    image = CharField()
    description = TextField()
    ingredients = TextField()
    instructions = TextField()
    average_rating = IntegerField(default=0)

    class Meta:
        database = DATABASE

class Reviews(Model):
    rating = IntegerField(default=0)
    date_reviewed = DateTimeField(default=datetime.datetime.now)
    comment = TextField()
    user_id = ForeignKeyField(User, backref="users") 
    recipe_id = ForeignKeyField(Recipe, backref="recipes") 
    
    class Meta:
        database = DATABASE
        order_by = ('-date_reviewed',)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Reviews], safe=True)
    DATABASE.close()

    