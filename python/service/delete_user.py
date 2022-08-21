import os
import sys
import pymongo
from bson import ObjectId

client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
db = client.recallico


def print_usage():
    print('Usage: python delete_user.py <username or id>')


def delete_user(user):
    userid = ObjectId(user)
    db.users.delete_one({'_id': userid})


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
        exit(1)

    delete_user(sys.argv[1])
