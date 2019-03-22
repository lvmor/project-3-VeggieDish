from datetime import datetime
from veggieproject import db

from peewee import *

# DATABASE = SqliteDatabase('veggiedish.db')



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    reviews = db.relationship('Review', backref='author', lazy=True) #This sets relationship between user and reviews

#This shows how our user object looks when printed out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #user.id here refers to id of user(author) 


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"




# class User(Model):
#     full_name = TextField()
#     avatar = TextField()

#     city = TextField()
#     date_joined = DateTimeField(default=datetime.datetime.now)

#     class Meta:
#         database = DATABASE
#         order_by = ('-date_joined',)

# class Recipe(Model):
#     name = CharField()
#     image = CharField()
#     description = TextField()
#     ingredients = TextField()
#     instructions = TextField()
#     average_rating = IntegerField(default=0)

#     class Meta:
#         database = DATABASE

# class Review(Model):
#     rating = IntegerField(default=0)
#     date_reviewed = DateTimeField(default=datetime.datetime.now)
#     comment = TextField()
#     # user_id = ForeignKeyField(model=User, backref="users") 
#     recipe_id = ForeignKeyField(model=Recipe, backref="recipes") 
    
#     class Meta:
#         database = DATABASE
#         order_by = ('-date_reviewed',)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Review], safe=True)
    DATABASE.close()

    