#!/bin/sh

echo "Waiting for postgres..."

#loop continues until something like Connection to api-db port 5432 [tcp/postgresql] succeeded! is returned
while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0