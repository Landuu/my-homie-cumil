from flask import Flask
from tweety import Twitter
  
app = Flask(__name__)
app.debug = True

def filter_retweets(var):
    return hasattr(var, "is_retweet") and not var.is_retweet

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    tw = Twitter("session")
    tw.start('email@gmail.com', 'password')
    tweets = tw.get_tweets(username="2Dgirlenjoyer", replies=False)
    
    filtered = filter(filter_retweets, tweets)
    for tweet in filtered:
        print(tweet)

    return 'Test'

if __name__ == '__main__':
   app.run()