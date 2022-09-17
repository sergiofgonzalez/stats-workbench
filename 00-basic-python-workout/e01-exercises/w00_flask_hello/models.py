import sqlite3
from sqlite3 import Error

def drop_table():
    with sqlite3.connect("songs.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""DROP TABLE IF EXISTS songs;""")
    return True

def create_db():
    with sqlite3.connect("songs.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE songs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                artist TEXT NOT NULL,
                title TEXT NOT NULL,
                rating INTEGER NOT NULL
            );
        """)
    return True

# This will execute if invoked as `python models.py`
if __name__ == "__main__":
    # create_connection()
    drop_table()
    create_db()
