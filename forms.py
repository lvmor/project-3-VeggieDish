from flask_wtf import FlaskForm as Form

from wtforms import TextField, TextAreaField, SubmitField, PasswordField, FileField, StringField, IntegerField


# from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
#                                Length, EqualTo)

from models import User, Recipe, Review


#images = UploadSet('images', IMAGES)

class UserForm(Form):
    full_name =  TextField("Your Full Name")
    avatar = StringField()
    city = TextField()
    submit = SubmitField('Edit Profile')

class RecipeForm(Form):
    name = TextField("Recipe Name")
    # image = FileField('image', validators=[
    #     FileRequired(),
    #     FileAllowed(images, 'Images only!')
    # ])
    image = StringField("url for image")

    description = TextAreaField("Recipe Description")
    ingredients = TextAreaField("Recipe Ingredients")
    instructions = TextField("Recipe Instructions")
    submit = SubmitField('Create Recipe')

class ReviewForm(Form):
    rating = IntegerField("Recipe Rating on a scale of 1-5")
    comment = TextAreaField("Review of Recipe")
