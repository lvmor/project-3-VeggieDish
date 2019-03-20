from flask import Flask, g
from flask import render_template, flash, redirect, url_for

import json
import models
from forms import RecipeForm

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

# login_manager = LoginManager()
# ## sets up our login for the app
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(userid):
#     try:
#         # get the user if the user exists in the system
#         return models.User.get(models.User.id == userid)
#     except models.DoesNotExist:
#         return None


# @app.before_request
# def before_request():
#     g.db = models.DATABASE
#     g.db.connect()

# @app.after_request
# def after_request():
#     g.db.close()
#     return response

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
            return render_template('users.html', user_template = users_data)
        else:
            user_ID = int(user_id)
            return render_template('user.html', user = users_data[user_ID])

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
            return render_template('review.html', review = reviews_data[review_ID])

@app.route('/recipes')
@app.route('/recipes/')
@app.route('/recipes/<recipe_id>')
def recipes(recipe_id = None):
    if recipe_id == None:
        recipes = models.Recipe.select().limit(10)
        print(recipes)
        return render_template("recipes.html", recipes_template = recipes)
    else:
        recipe_id = int(recipe_id)
        recipe = models.Recipe.get(models.Recipe.id == recipe_id)
        return render_template("recipe.html", recipe=recipe)

@app.route('/create-recipe', methods=['GET', 'POST'])
def recipe_form():
    form = RecipeForm()
    if form.validate_on_submit():
        models.Recipe.create(
            name=form.name.data.strip(), 
            description=form.description.data.strip(),
            ingredients=form.ingredients.data.strip(),
            instructions=form.instructions.data.strip(),
            image=form.image.data.strip()
        )
        flash("New recipe created. Called: {}".format(form.name.data))
        return redirect('/recipes')
    else:
        return render_template('recipe_form.html', form=form)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
