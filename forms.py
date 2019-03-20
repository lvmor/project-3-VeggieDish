from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField, IntegerField
from models import User, Recipe, Review


class UserForm(Form):
    full_name =  TextField("Your Full Name")
    avatar = TextField()
    submit = SubmitField('Edit Profile')

class RecipeForm(Form):
    name = TextField("Recipe Name")
    description = TextAreaField("Recipe Description")
    ingredients = TextAreaField("Recipe Ingredients")
    instructions = TextField("Recipe Instructions")
    submit = SubmitField('Create Recipe')

class ReviewForm(Form):
    rating = IntegerField("Recipe Rating on a scale of 1-5")
    comment = TextAreaField("Review of Recipe")
    submit = SubmitField('Submit')
    