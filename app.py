from flask import Flask, g
from flask import render_template, flash, redirect, url_for
import json

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

# @app.route('/users')
# @app.route('/users/')
# @app.route('/users/<user_id>')
# def users(user_id = None):
#     with open('users.json') as json_data:
#         users_data = json.load(json_data)
#         if user_id == None:
#             return render_template('users.html', user_template = users_data)
#         else:
#             user_ID = int(user_id)
#             return render_template('user.html', user = users_data[user_ID])

@app.route('/users')
@app.route('/users/')
@app.route('/users/<user_id>', methods = ['GET', 'POST'])
def users(user_id = None):
    form = UserForm()
    if form.validate_on_submit():
        models.User.create( 
            avatar = form.avatar.strip(), 
            full_name = form.full_name.strip())

        flash("Name changed to: {}".format(form.full_name))
        return redirect('/users')

    return render_template("new_user.html", title="New User", form=form)

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

# @app.route('/reviews')
# @app.route('/reviews/')
# @app.route('/reviews/<review_id>', methods = ['GET', 'POST'])
# def reviews(review_id = None):
#     form = ReviewForm()
#     if form.validate_on_submit():
#         models.Review.create(
#             rating = form.rating.data.strip(), 
#             comment = form.comment.strip())
#         flash("New comment and rating: {}".format(form.full_name.data))
#         return redirect('/reviews/')

#     return render_template("new_user.html", title="New Review", form=form)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

