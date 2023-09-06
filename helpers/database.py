from . import Config
import mysql.connector

def get_database():
    config = Config()
    return mysql.connector.connect(
        host=config.db_host,
        user=config.db_user,
        password=config.db_password,
        database=config.db_user
    )

def reset_database():
    db = get_database()
    dbc = db.cursor()
    dbc.execute("DROP TABLE IF EXISTS Tweets")
    dbc.execute("CREATE TABLE IF NOT EXISTS Tweets (Id BIGINT PRIMARY KEY, Responded BOOLEAN)")