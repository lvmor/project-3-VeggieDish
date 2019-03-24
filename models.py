import datetime
from peewee import *

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

import os

from playhouse.db_url import connect

DATABASE = SqliteDatabase('veggiedish.db')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length = 100)
    full_name = TextField()
    avatar = TextField()
    city = TextField()
    #comes from backend - do not need in forms
    date_joined = DateTimeField(default= str(datetime.datetime.now)[0:10])

    class Meta:
        database = DATABASE
        order_by = ('-date_joined',)

    @classmethod
    def create_user(cls, username, email, password, full_name, avatar, city):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                full_name= full_name,
                avatar = avatar,
                city= city
                )
        except IntegrityError:
            raise ValueError("User/Email already exists")

class Recipe(Model):
    name = CharField()
    image = CharField()
    description = TextField()
    ingredients = TextField()
    instructions = TextField()
    average_rating = IntegerField(default=0)
    user_id = ForeignKeyField(model=User, backref="users")

    class Meta:
        database = DATABASE

class Review(Model):
    rating = IntegerField(default=0)
    date_reviewed = DateTimeField(default=datetime.datetime.now)
    comment = TextField()
    user_id = ForeignKeyField(model=User, backref="users") 
    recipe_id = ForeignKeyField(model=Recipe, backref="recipes") 
    
    class Meta:
        database = DATABASE
        order_by = ('-date_reviewed',)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Review], safe=True)
    DATABASE.close()

    