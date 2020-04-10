#!/bin/bash

until [ echo > /dev/tcp/$DB_HOST/$DB_PORT ]
do
    sleep 1
done

echo "Database accepting connections."
exec "$@"
