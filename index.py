from flask import Flask
from tweety import Twitter
  
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    tw = Twitter("session")
    tw.start('email@gmail.com', 'password')
    all_tweets = tw.get_tweets("2Dgirlenjoyer")
    for tweet in all_tweets:
        print(tweet)

    return 'Test'

if __name__ == '__main__':
   app.run()