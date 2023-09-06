import os

class EnvConfig:
    def __init__(self):
        self.username = os.getenv("TW_USERNAME")
        self.password = os.getenv("TW_PASSWORD")
        self.extra = os.getenv("TW_EXTRA")
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")