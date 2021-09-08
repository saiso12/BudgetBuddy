#!/bin/ sh

echo "Waiting for Postgres to load..."

# loop until the port is up! `Connection to web-db port 5432 [tcp/postgresql] succeeded!`
while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started..."

exec "$@"