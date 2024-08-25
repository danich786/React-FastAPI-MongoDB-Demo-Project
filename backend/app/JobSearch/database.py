
from pymongo.mongo_client import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env file


# Create a new client and connect to the server
client = MongoClient(os.environ.get("MONGO_DB_URI"))

db = client[os.environ.get("MONGO_DB_DATABASE")]
