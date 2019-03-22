#This is importing the __init__ file from within veggieproject package
from veggieproject import app

DEBUG = True
PORT = 8000


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
