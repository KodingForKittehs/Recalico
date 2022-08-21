import os
import pymongo

client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
db = client.recallico

if __name__ == '__main__':
    print(db.list_collection_names())
