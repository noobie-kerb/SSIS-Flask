import mysql.connector
from config import secretKey, databaseHost, databaseName, databasePassword, databaseUser, BOOTSTRAP_SERVE_LOCAL
from mysql.connector import connect, Error


def database_connect():
    try:
        db = connect(
            host = databaseHost,
            user = databaseUser,
            password = databasePassword,
            database = databaseName
        )
        cursor = db.cursor()
        return db, cursor
    except Error as e:
        print(f"Error connection: {e}")