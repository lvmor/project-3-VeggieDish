#This is importing app from the __init__ file from within veggieproject package
from veggieproject import app


# from flask_login import LoginManager, login_user, logout_user, login_required, current_user



# import json
# import functools
# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for
# )

DEBUG = True
PORT = 8000


# app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'


# @app.before_request
# def before_request():
#     g.db = models.DATABASE
#     g.db.connect()

# @app.after_request
# def after_request(response):
#     g.db.close()
#     return response

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
