from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

mongo_uri = f"mongodb://127.0.0.1:27017"

client = MongoClient(mongo_uri, server_api=ServerApi('1'))

db = client.youtubedump
videos_db = db["videos"]
playlists_db = db["playlists"]
