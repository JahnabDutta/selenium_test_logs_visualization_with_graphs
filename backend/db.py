import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["network_logs"]
collection = db["network_logs"]

