import pymongo
from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")


client = pymongo.MongoClient(db_host)
db = client[db_name]
collection = db[collection_name]

