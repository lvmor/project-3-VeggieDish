import datetime
from peewee import *

DATABASE = SqliteDatabase('veggiedish.db')

class User(Model):
    full_name = TextField()
    avatar = TextField()

    city = TextField()
    date_joined = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-date_joined',)

class Recipe(Model):
    name = CharField()
    # image = CharField()
    description = TextField()
    ingredients = TextField()
    instructions = TextField()
    average_rating = IntegerField(default=0)

    class Meta:
        database = DATABASE

class Review(Model):
    rating = IntegerField(default=0)
    date_reviewed = DateTimeField(default=datetime.datetime.now)
    comment = TextField()
    # user_id = ForeignKeyField(model=User, backref="users") 
    recipe_id = ForeignKeyField(model=Recipe, backref="recipes") 
    
    class Meta:
        database = DATABASE
        order_by = ('-date_reviewed',)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Review], safe=True)
    DATABASE.close()

    