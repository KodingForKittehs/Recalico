#!/bin/bash

DB_URL="mongodb+srv://kodingforkittehs:${RECALLICO_PASS}@recallico.enfadfj.mongodb.net/test?retryWrites=true&w=majority"
docker run --rm -i --network=host mongo mongosh "$DB_URL" << EOL
    use test
    db.test.insertOne({'test': 'test'});
    db.test.find({});
EOL