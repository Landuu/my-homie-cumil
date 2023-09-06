import os
from tweety import Twitter
from .database import get_database


def create_session(extra = None):
    config = EnvConfig()
    tw = Twitter('user')
    tw.start(username=config.username, password=config.password, extra=extra)
    return tw


def get_login_lock():
    db = get_database()
    dbc = db.cursor()
    dbc.execute("SELECT Value FROM Helpers WHERE Id = 'Lock' LIMIT 1")
    row = dbc.fetchone()
    
    if(row is None):
        return False
    return row[0] == '1'


def set_login_lock(state):
    db = get_database()
    dbc = db.cursor()
    value = '1' if state else '0'
    dbc.execute("UPDATE Helpers SET Value = %s WHERE Id = 'Lock'", [value])
    db.commit()


def parse_tweets():
    if(get_login_lock()):
        return

    try:
        tw = create_session()
    except:
        set_login_lock(True)
        return
    
    tweets = tw.get_tweets(username="2Dgirlenjoyer", replies=False)
    filtered = []
    for tweet in tweets:
        if hasattr(tweet, "is_retweet") and not tweet.is_retweet:
            filtered.append(tweet)

    for f in filtered:
        print(f)


