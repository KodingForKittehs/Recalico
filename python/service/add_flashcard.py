import os
import sys
import pymongo
from bson import ObjectId
from bson.errors import InvalidId
import users

client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
db = client.recallico


def print_usage():
    print('Usage: python add_flashcard.py <username> <question> <answer>')


def add_flashcard(user, question, answer):
    if not user:
        print('User is missing')
        return
    if not question:
        print('Question is missing')
        return
    if not answer:
        print('Answer is missing')
        return

    try:
        userid = ObjectId(user)
    except InvalidId:
        userid = users.get_user_id(db, user)

    if not userid:
        raise Exception(f'User "{user}" does not exist')

    db.flashcards.insert_one({
        'userid': userid,
        'question': question,
        'answer': answer
    })


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print_usage()
        exit(1)

    add_flashcard(sys.argv[1], sys.argv[2], sys.argv[3])
