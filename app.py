from flask import Flask, g
from flask import render_template, flash, redirect, url_for
import json


# ReviewForm, RecipeForm, UserForm to be included into app later
from forms import RegistrationForm, LoginForm
import models

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

#Config for secret key
app.config['SECRET_KEY'] = '8c1577e01307f04f3d91a2a6c6450f31'

@app.route('/')
def index():
    with open('recipes.json') as json_data:
        recipes_data = json.load(json_data)
        return render_template('recipes.html', recipes_template = recipes_data)

@app.route('/users')
@app.route('/users/')
@app.route('/users/<user_id>')
def users(user_id = None):
    with open('users.json') as json_data:
        users_data = json.load(json_data)
        if user_id == None:
            return render_template('users.html', user_template = user_data)
        else:
            user_ID == int(user_id)
            return render_template('user.html', user_item = users_data[user_ID])

@app.route('/reviews')
@app.route('/reviews/')
@app.route('/reviews/<review_id>')
def reviews(review_id = None):
    with open('reviews.json') as json_data:
        reviews_data = json.load(json_data)
        if review_id == None:
            return render_template('reviews.html', reviews_template = reviews_data)
        else:
            review_ID = int(review_id)
            return render_template('review.html', review_item = reviews_data[review_ID])

@app.route('/recipes')
@app.route('/recipes/')
@app.route('/recipes/<recipe_id>')
def recipes(recipe_id = None):
    with open('recipes.json') as json_data:
        recipes_data = json.load(json_data)
        if recipe_id == None:
            return render_template('recipes.html', recipes_template = recipes_data)
        else:
            recipe_ID = int(recipe_id)
            return render_template('recipe.html', recipe = recipes_data[recipe_ID])


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)

