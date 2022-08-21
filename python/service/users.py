def get_user_id(db, username):
    user = db.users.find_one({'username': username}, {'_id': 1})
    return user['_id'] if user else None
