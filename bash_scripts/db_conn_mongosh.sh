#!/bin/bash

DB_URL="mongodb+srv://kodingforkittehs:${RECALLICO_PASS}@recallico.enfadfj.mongodb.net/recallico?retryWrites=true&w=majority"
docker run --rm -it --network=host mongo mongosh "$DB_URL"