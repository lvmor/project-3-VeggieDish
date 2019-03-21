from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError, NumberRange

from models import User, Recipe, Review



#images = UploadSet('images', IMAGES)

class UserForm(Form):
    id = IntegerField()
    full_name =  TextField("Your Full Name")
    avatar = StringField()
    city = TextField()
    submit = SubmitField('Delete Profile')
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
    rating = IntegerField("Recipe Rating on a scale of 1-5",
        validators=[
            NumberRange(min=1, max=5, message="Please enter a number between 1 and 5")
        ])
    comment = TextAreaField("Review of Recipe")
    submit = SubmitField('Create Review')


class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')