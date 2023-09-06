import os
from flask import Flask, request
from dotenv import load_dotenv
from helpers import EnvConfig, reset_database, parse_tweets, create_session, get_login_lock, set_login_lock


app = Flask(__name__)
app.debug = True
load_dotenv()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/debug')
def debug():
    print(get_login_lock())
    return 'ok'

@app.route('/init')
def init():
    reset_database()
    return 'Ok'

@app.route('/session/<code>')
def session(code):
    create_session(str(code))
    set_twitter_lock(False)
    return 'Session created'

@app.route('/test')
def test():
    parse_tweets()
    return 'Parsed'


if __name__ == '__main__':
    app.run()