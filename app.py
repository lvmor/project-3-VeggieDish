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

