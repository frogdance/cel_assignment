# Use official PostgreSQL image as base
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres


# Copy SQL script for initializing database
COPY init.sql /docker-entrypoint-initdb.d/init.sql
