from flask_wtf import FlaskForm as Form

from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, FileField, IntegerField, HiddenField, SelectField
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
    id = HiddenField()
    rating = SelectField(u"Recipe Rating ", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    comment = TextAreaField("Review of Recipe")
    submit = SubmitField('Create Review')

def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')
 
class RegistrationForm(Form):
    full_name = StringField("Your full name", validators=[DataRequired()])
    avatar = StringField("Your avatar")
    city = StringField("Your city", validators=[DataRequired()])
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            #name_exists calls the above method to make sure user doesn't already exist
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=3),
            EqualTo('confirm_password', message='Passwords must match')
        ])

    confirm_password = PasswordField(
        'Confirm password', 
        validators=[DataRequired()]
        )

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])



class UpdateAccountForm(Form):
    full_name = StringField("Your full name", validators=[DataRequired()])
    avatar = StringField("Your avatar")
    city = StringField("Your city", validators=[DataRequired()])
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            #name_exists calls the above method to make sure user doesn't already exist
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    submit = SubmitField('Edit Profile')


# Set up validators for these afterwards  
# full_name =  TextField("Your Full Name")
#     avatar = StringField()
#     city = TextField()
#     submit = SubmitField('Delete Profile')
#     submit = SubmitField('Edit Profile')