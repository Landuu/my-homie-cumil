from .config import EnvConfig
import mysql.connector

def get_database():
    config = EnvConfig()
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
    dbc.execute("CREATE TABLE IF NOT EXISTS Tweets (Id BIGINT PRIMARY KEY)")
    dbc.execute("DROP TABLE IF EXISTS Helpers")
    dbc.execute("CREATE TABLE IF NOT EXISTS Helpers (Id varchar(255) PRIMARY KEY, Value varchar(255))")
    dbc.execute("INSERT INTO Helpers VALUES('Lock', '0')")
    db.commit()