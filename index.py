import os
from flask import Flask
from tweety import Twitter
from dotenv import load_dotenv

app = Flask(__name__)
app.debug = True
load_dotenv()

def filter_retweets(var):
    return hasattr(var, "is_retweet") and not var.is_retweet

@app.route('/')
def hello_world():
    print(os.getenv("TW_USERNAME"))
    return 'Hello World! '

@app.route('/test')
def test():
    tw = Twitter("session")
    tw.start(os.getenv('TW_USERNAME'), os.getenv('TW_PASSWORD'), extra=os.getenv('TW_EXTRA'))
    tweets = tw.get_tweets(username="2Dgirlenjoyer", replies=False)
    
    filtered = filter(filter_retweets, tweets)
    for tweet in filtered:
        print(tweet)

    return 'Test'

if __name__ == '__main__':
   app.run()