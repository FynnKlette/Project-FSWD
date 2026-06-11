import sqlite3

'''
# Create DB
conn = sqlite3.connect("tauschdaten.db")
conn.close()
'''

# DB Connector
db_path = "tauschdaten.db"

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Create Tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studiengang (
        studiengang TEXT NOT NULL PRIMARY KEY
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studienbüro_ma (
        ma-id TEXT NOT NULL PRIMARY KEY,
        vorname TEXT,
        name TEXT,
        email TEXT,
        password TEXT
    )
    """)

conn.commit()

