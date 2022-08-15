import os
import pymongo
import sys

client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
db = client.recallico


def add_flashcard(user, question, answer):
    if not user:
        print('Username is missing')
        return
    if not question:
        print('Question is missing')
        return
    if not answer:
        print('Answer is missing')
        return

    pass


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Expected 3 arguments')
        exit(1)

    add_flashcard(sys.argv[0], sys.argv[1]. sys.argv[2])
