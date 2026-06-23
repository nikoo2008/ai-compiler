import sqlite3


def execute_runtime():

    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        email TEXT,
        role TEXT
    )
    """)

    conn.commit()

    conn.close()

    return "Database created"