from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

#Configs
app.config['SECRET_KEY'] = '8c1577e01307f04f3d91a2a6c6450f31'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veggiedish.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from veggieproject import routes
