#!/bin/bash

# `mongo` is deprecated in favor of `mongosh`
DB_URL="mongodb+srv://kodingforkittehs:${RECALLICO_PASS}@recallico.enfadfj.mongodb.net/recallico?retryWrites=true&w=majority"
docker run --rm -it --network=host mongo mongo "$DB_URL"