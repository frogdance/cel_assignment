import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port = "5432")