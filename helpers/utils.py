import os
from tweety import Twitter
from .database import get_database
from .config import EnvConfig
import smtplib, ssl


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


def send_email_notification():
    config = EnvConfig()
    email_ctx = ssl.create_default_context()
    with smtplib.SMTP(config.smtp_ip, config.smtp_port) as server:
        server.ehlo()
        server.starttls(context=email_ctx)
        server.ehlo()
        server.login(config.smtp_login, config.smtp_password)
        server.sendmail(config.smtp_login, 'landuscam@gmail.com', "spardl z rowerka")


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


