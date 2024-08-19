from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
MON_NAME = os.environ.get("MON_NAME")
MON_PASS = os.environ.get("MON_PASS")
MON_APP_NAME = os.environ.get("MON_APP_NAME")