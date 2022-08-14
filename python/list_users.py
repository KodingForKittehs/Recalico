import os
import pymongo

mongodb_url = os.environ.get('MONGODB_URL')
client = pymongo.MongoClient(mongodb_url)
