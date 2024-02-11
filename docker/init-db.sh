#!/bin/bash

set -e

set +a
source /docker-entrypoint-initdb.d/.env
set -a

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<- EOSQL

CREATE ROLE $USER
  WITH PASSWORD 'lasiusdev'
	CREATEDB
	CREATEROLE
	LOGIN
	CONNECTION LIMIT -1;

CREATE DATABASE $DATABASE
  WITH OWNER $USER
  TEMPLATE = 'template0'
  ENCODING = 'UTF-8'
  LC_COLLATE = 'hu_HU.UTF-8'
  LC_CTYPE = 'hu_HU.UTF-8'
  TABLESPACE = pg_default
  CONNECTION LIMIT = -1;

GRANT ALL ON SCHEMA public TO $USER;

EOSQL