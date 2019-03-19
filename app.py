from flask import Flask, g
from flask import render_template, flash, redirect, url_for
import json

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

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

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)

