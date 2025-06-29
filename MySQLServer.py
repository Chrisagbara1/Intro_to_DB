# MySQLServer.py

import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error as MySQLError  

from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

def create_database():
    db_password = os.getenv("DB_PASSWORD")

    if not db_password:
        print("Error: 'DB_PASSWORD' not found in environment.")
        return

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print("Error while connecting to MySQL:", err)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()