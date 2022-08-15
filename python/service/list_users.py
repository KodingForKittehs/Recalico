import os
import pymongo

client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
db = client.recallico

for user in db.users.find({}):
    print(user)
