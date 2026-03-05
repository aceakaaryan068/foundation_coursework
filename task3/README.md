Task 3 — Docker Setup (PostgreSQL)
This runs PostgreSQL in Docker and automatically applies:

schema.sql — creates the 3 normalised tables
queries.sql — inserts data and runs all queries

Prerequisites

Docker
Docker Compose

Start Database
From the task3 folder:
docker compose up -d
This starts PostgreSQL with:

Database: clubdb
User: clubuser
Password: clubpass
Port: 5432

On first startup Docker automatically runs schema.sql then queries.sql.
Open psql Shell
docker compose exec postgres psql -U clubuser -d clubdb
Re-run Queries Manually
docker compose exec postgres psql -U clubuser -d clubdb -f /docker-entrypoint-initdb.d/02_queries.sql
Stop Database
docker compose down
Stop and Remove All Data (Fresh Start)
docker compose down -v