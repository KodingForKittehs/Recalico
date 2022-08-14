#!/bin/bash

[[ -z $1 ]] && echo "Username required" && exit 1
[[ -z $2 ]] && echo "Question required" && exit 1
[[ -z $3 ]] && echo "Answer required" && exit 1

DB_URL="mongodb+srv://kodingforkittehs:${RECALLICO_PASS}@recallico.enfadfj.mongodb.net/recallico?retryWrites=true&w=majority"
docker run --rm -i --network=host mongo mongosh "$DB_URL" << EOL
    let user = db.users.findOne({usename:"$1"});
    if (!user) {
        print("User does not exist: " + $1);
        exit;
    }
    db.flashcards.insertOne({
        'username': "$1",
        'question': "$2",
        'answer': "$3",
    });
EOL