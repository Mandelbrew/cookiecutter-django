--
-- PostgreSQL application database creation
--

SET client_encoding = 'UTF8';

SET default_transaction_read_only = OFF;
SET standard_conforming_strings = ON;

DROP DATABASE ${DB_NAME};
DROP ROLE ${DB_USER};

CREATE ROLE ${DB_USER} WITH PASSWORD '${DB_PASSWORD}' CREATEROLE CREATEDB LOGIN;
GRANT ${DB_USER} TO ${DB_ROOT};

CREATE DATABASE ${DB_NAME} WITH OWNER ${DB_USER} TEMPLATE = template0;
