import os

class EnvConfig:
    def __init__(self):
        self.username = os.getenv("TW_USERNAME")
        self.password = os.getenv("TW_PASSWORD")
        self.extra = os.getenv("TW_EXTRA")
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.smtp_ip = os.getenv("SMTP_IP")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.smtp_login = os.getenv("SMTP_LOGIN")
        self.smtp_password = os.getenv("SMTP_PASSWORD")