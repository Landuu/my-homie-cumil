import os
from tweety import Twitter

class Config:
    def __init__(self):
        self.username = os.getenv("TW_USERNAME")
        self.password = os.getenv("TW_PASSWORD")
        self.extra = os.getenv("TW_EXTRA")
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")


def create_session(extra = None):
    config = Config()
    tw = Twitter("session")
    tw.start(username=config.username, password=config.password)
    return tw


def parse_tweets():
    tw = create_session()
    tweets = tw.get_tweets(username="2Dgirlenjoyer", replies=False)

    filtered = []
    for tweet in tweets:
        if hasattr(tweet, "is_retweet") and not tweet.is_retweet:
            filtered.append(tweet)

    for f in filtered:
        print(f)


