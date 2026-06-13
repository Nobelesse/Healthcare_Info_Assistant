import sqlite3


DB_NAME = "healthcare.db"


def get_connection():

    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rating INTEGER,
            feedback TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT
        )
    """)

    conn.commit()

    conn.close()