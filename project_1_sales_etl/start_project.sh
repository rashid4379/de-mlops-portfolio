#!/bin/bash

echo "Starting PostgreSQL container..."
docker compose up -d

echo "Waiting for PostgreSQL to be ready..."
sleep 5

echo "Checking running containers..."
docker ps

echo "Creating tables..."
docker exec -i sales_postgres psql -U rashid -d salesdb < sql/create_tables.sql

echo "Loading sample data and running basic queries..."
docker exec -i sales_postgres psql -U rashid -d salesdb < sql/basic_queries.sql

echo "Testing Python database connection..."
python scripts/test_connection.py

echo "Project startup complete."