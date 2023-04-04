import pymongo
from dotenv import load_dotenv
import os
from elasticsearch import Elasticsearch

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")

elastic_search_host = os.getenv("ELASTIC_SEARCH_HOST")
elastic_search_port = os.getenv("ELASTIC_SEARCH_PORT")


client = pymongo.MongoClient(db_host)
db = client[db_name]
collection = db[collection_name]

#instantiate elastic search client with host port and scheme
es_client = Elasticsearch("https://"+elastic_search_host+":"+elastic_search_port+"/")

