from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from config import MON_NAME, MON_PASS, MON_APP_NAME

client = MongoClient(f"mongodb+srv://{MON_NAME}:{MON_PASS}@webhistorymaps.lpibk.mongodb.net/?retryWrites=true&w=majority&appName={MON_APP_NAME}")

db = client.WebHistoryEventAreas

collection_name = db["EventsArea"]
# Create a new client and connect to the server
