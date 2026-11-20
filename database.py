
import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="umbb_university",
        user="postgres",
        password="mot de passe",
        port="5432"
    )

    return connection
