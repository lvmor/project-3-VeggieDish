from flask import Flask, g
from flask import render_template, flash, redirect, url_for

import json
import models
from forms import RecipeForm, UserForm

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from forms import UserForm, RecipeForm, ReviewForm

import functools
import models


# ReviewForm, RecipeForm, UserForm to be included into app later
from forms import RegistrationForm, LoginForm
import models

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

#Config for secret key
app.config['SECRET_KEY'] = '8c1577e01307f04f3d91a2a6c6450f31'

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
    return render_template("home.html", recipes_template=recipe_data)

@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/users')
@app.route('/users/')
@app.route('/users/<user_id>', methods=['GET', 'POST'])
def users(user_id = None):
    if user_id == None:
        users_data = models.User.select().limit(5)
        return render_template('users.html', users_template = users_data)
    else:
        user_id = int(user_id)
        user_data = models.User.get(models.User.id == user_id)
        
        form = UserForm()
        if form.validate_on_submit():
            models.User.create( 
                avatar = form.avatar.data.strip(), 
                full_name = form.full_name.data.strip(),
                city = form.city.data.strip())
            flash("Name changed to: {}".format(form.full_name))
            return redirect('/users/')
        
        return render_template("new_user.html", title="New User", form=form, user=user_data)

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
@app.route('/recipes/', methods=['GET', 'POST'])
@app.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def recipes(recipe_id = None):
    if recipe_id == None:

        # this is list of recipes we show in page
        recipes = models.Recipe.select().limit(10)

        # this is add/update form for recipe
        form = RecipeForm()
        
        # receive recipe id and command from recipes list
        recipeid = request.form.get('recipeid', '')
        command = request.form.get('submit', '')

        if command == 'Delete':
            models.Recipe.delete_by_id(recipeid)
            return redirect("/recipes")
        elif command == 'Edit':
            recipeid = int(recipeid)
            recipe = models.Recipe.get(models.Recipe.id == recipeid)
            form.id.data = recipe.id
            form.name.data = recipe.name
            form.image.data = recipe.image
            form.description.data = recipe.description
            form.ingredients.data = recipe.ingredients
            form.instructions.data = recipe.instructions

            return render_template("recipes.html", recipes_template=recipes, form=form)

        if form.validate_on_submit():
            if form.id.data == '': # Create new
                models.Recipe.create(
                    name=form.name.data.strip(), 
                    description=form.description.data.strip(),
                    ingredients=form.ingredients.data.strip(),
                    instructions=form.instructions.data.strip(),
                    image=form.image.data.strip()
                )
                flash("New recipe created. Called: {}".format(form.name.data))
            else: # Update Recipe
                recipe = models.Recipe.get(models.Recipe.id == form.id.data)
                recipe.name = form.name.data.strip()
                recipe.image = form.image.data.strip()
                recipe.description = form.description.data.strip()
                recipe.ingredients = form.ingredients.data.strip()
                recipe.instructions = form.instructions.data.strip()
                recipe.save()
                flash("recipe updated")
            return redirect('/recipes')

        return render_template("recipes.html", recipes_template=recipes, form=form)
    else: # Recipe Details
        recipe_id = int(recipe_id)
        recipe = models.Recipe.get(models.Recipe.id == recipe_id)
        reviews_template = models.Review.select().where(models.Review.recipe_id == recipe_id)
        
        form = ReviewForm()

        reviewsid = request.form.get('reviewsid', '')
        command = request.form.get('submit', '')

        if command == 'Delete':
            models.Review.delete_by_id(reviewsid)
            return redirect('/recipes/{}'.format(recipe_id))
 

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

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Signup', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@site.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
