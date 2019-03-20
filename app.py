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

from forms import UserForm, RecipeForm, ReviewForm

import functools
import models

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    recipe_data = models.Recipe.select().limit(100)
    return render_template("recipes.html", recipes_template=recipe_data)

@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/users')
@app.route('/users/')
@app.route('/users/<user_id>', methods = ['GET', 'POST'])
def users(user_id = None):
    form = UserForm()
    if form.validate_on_submit():
        models.User.create( 
            avatar = form.avatar.strip(), 
            full_name = form.full_name.strip(),
            city = form.city.strip(),)

        flash("Name changed to: {}".format(form.full_name))
        return redirect('/users')

    return render_template("new_user.html", title="New User", form=form)

@app.route('/reviews')
@app.route('/reviews/')
@app.route('/reviews/<review_id>')
def reviews(review_id = None):
    if review_id == None:
        reviews = models.Review.select().limit(10)
        return render_template("reviews.html", reviews_template = reviews)
    else:
        review_id = int(review_id)
        review = models.Reviews.get(models.Reviews.id == review_id)
        return render_template("reviews.html", reviews=reviews)


@app.route('/recipes')
@app.route('/recipes/')
@app.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def recipes(recipe_id = None):
    if recipe_id == None:
        recipes = models.Recipe.select().limit(10)
        return render_template("recipes.html", recipes_template=recipes)
    else:
        recipe_id = int(recipe_id)
        recipe = models.Recipe.get(models.Recipe.id == recipe_id)
        reviews_template = models.Review.select().where(models.Review.recipe_id == recipe_id)
        
        form = ReviewForm()
        if form.validate_on_submit():
            ratingInt = int(form.rating.data)
            models.Review.create(
                rating=ratingInt, 
                comment=form.comment.data.strip(),
                recipe_id = recipe_id
            )
            return redirect('/recipes/{}'.format(recipe_id))
        else:
            return render_template("review_form.html", recipe=recipe, form=form, reviews_template=reviews_template)

@app.route('/create-recipe', methods=['GET', 'POST'])
#function name needs to match the link
def recipe_form():
    form = RecipeForm()
     #same name as imported form
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
