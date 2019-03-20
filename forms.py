# from flask_wtf import FlaskForm as Form
# from wtforms import TextField, TextAreaField, SubmitField, PasswordField, FileField, IntegerField,  FileRequired

# from models import User, Recipe, Reviews

# # images = UploadSet('images', IMAGES)

# class UserForm(Form):
#     full_name =  TextField("Your Full Name")
#     email =  TextField("Your email")
#     password = PasswordField("Password")
#     submit = SubmitField('Sign up')

# class RecipeForm(Form):
#     name = TextField("Recipe Name")
#     image = FileField('image', validators=[
#         FileRequired(),
#         FileAllowed(images, 'Images only!')
#     ])
#     description = TextAreaField("Recipe Description")
#     ingredients = TextAreaField("Recipe Ingredients")
#     instructions = TextField("Recipe Instructions")

# class ReviewForm(Form):
#     rating = IntegerField("Recipe Rating on a scale of 1-5")
#     comment = TextAreaField("Review of Recipe")

# from models import Reviews

# class ReviewForm(Form):
#     rating = IntegerField(default=0) 
#     review_comments = TextField()

# TextAreaField, SubmitField, IntegerField


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')




