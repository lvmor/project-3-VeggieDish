from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, FileField, FileAllowed, FileRequired

from models import User, Recipe, Review

images = UploadSet('images', IMAGES)

class UserForm(Form):
    full_name =  TextField("Your Full Name")
    email =  TextField("Your email")
    password = PasswordField("Password")
    submit = SubmitField('Sign up')

class RecipeForm(Form):
    name = TextField("Recipe Name")
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
    description = TextAreaField("Recipe Description")
    ingredients = TextAreaField("Recipe Ingredients")
    instructions = TextField("Recipe Instructions")

class ReviewForm(Form):
    rating = IntegerField("Recipe Rating on a scale of 1-5")
    comment = TextAreaField("Review of Recipe")
    