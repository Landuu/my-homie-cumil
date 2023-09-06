import os
from flask import Flask
from dotenv import load_dotenv
from helpers import Config, reset_database, parse_tweets, create_session


app = Flask(__name__)
app.debug = True
load_dotenv()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/init')
def init():
    reset_database()
    return 'Ok'

@app.route('/session')
def session():
    create_session()
    return 'Session created'

@app.route('/test')
def test():
    parse_tweets()
    return 'Parsed'


if __name__ == '__main__':
   app.run()