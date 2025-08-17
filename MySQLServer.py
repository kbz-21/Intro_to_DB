#!/usr/bin/python3
"""
MySQLServer.py
ALX Task: Create database alx_book_store
"""

import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (update user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # 🔹 replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create DB (won't fail if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
