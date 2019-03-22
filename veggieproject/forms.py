from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, FileField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from veggieproject.models import User

# from models import User
from veggieproject import models
# import models



#images = UploadSet('images', IMAGES)

class UserForm(Form):
    full_name =  TextField("Your Full Name")
    avatar = StringField()
    city = TextField()
    submit = SubmitField('Edit Profile')

class RecipeForm(Form):
    id = HiddenField()
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
    submit = SubmitField('Create Review')


class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a different one')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')