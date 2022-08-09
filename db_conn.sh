#!/bin/bash

DB_URL="mongodb+srv://kodingforkittehs:${RECALLICO_PASS}@recallico.enfadfj.mongodb.net/admin?retryWrites=true&w=majority"
echo $DB_URL
docker run --rm -it --network=host mongo mongo "$DB_URL"