from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, FileField, FileAllowed, FileRequired, StringField


from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)

from models import User, Recipe, Review


images = UploadSet('images', IMAGES)

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


# class UserForm(Form):
#     full_name =  TextField("Your Full Name")
#     email =  TextField("Your email")
#     password = PasswordField("Password")
#     submit = SubmitField('Sign up')


#this function handles validation of the user's name
def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')

class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            #this data is required!
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers, and underscores only.")
            ),
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            #wtForms email validator takes care of the long regex string for us! yay! hard to validate emails. especially if you have something like .ly or .me or .co.uk
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    