import psycopg2
import os
from dotenv import load_dotenv

def database_connection():
    try:
        load_dotenv()
        connection = psycopg2.connect(
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            database = os.getenv("DB_DATABASE")
        )

        return connection
    
    except Exception as error:
        print(f'Connection error: {error}')

if __name__ == '__main__':
    database_connection()