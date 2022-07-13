#!/bin/sh

echo "Waiting for postgres..."

# referenced the Postgres container using the name of the service, api-db
# loop continues until something like Connection to api-db port 5432 [tcp/postgresql] succeeded! is returned
#nc ( netcat ) command can be used to transfer arbitrary data over the network -z scans for listening daemons
while ! nc -z api-db 5432; do
    sleep 0.1
done

echo "PostgeSQL started"

python manage.py run -h 0.0.0.0