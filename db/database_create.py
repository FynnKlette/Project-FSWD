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
        ma_id TEXT NOT NULL PRIMARY KEY,
        vorname TEXT,
        name TEXT,
        email TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS modul (
        modul_id TEXT NOT NULL PRIMARY KEY,
        modulbezeichnung TEXT,
        etcs INT,
        sws INT,
        prüfungsform TEXT
    )
    """) 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS modulzuordnung (
        zuordnung_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        modul_id TEXT NOT NULL,
        studiengang TEXT NOT NULL,
                   
        FOREIGN KEY (modul_id) REFERENCES modul(modul_id),
        FOREIGN KEY (studiengang) REFERENCES studiengang(studiengang)
    )
    """) 


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studenten (
        username TEXT NOT NULL PRIMARY KEY,
        matrikelnummer INTEGER NOT NULL,
        name TEXT NOT NULL,
        vorname TEXT NOT NULL,
        email TEXT,
        password TEXT NOT NULL,
        studiengang TEXT,
                   
        FOREIGN KEY (studiengang) REFERENCES studiengang(studiengang)
    )
    """) 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kursangebot (
        kurs_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        kursbezeichnung TEXT NOT NULL,
        modul_id TEXT NOT NULL,
        semester TEXT NOT NULL,
        dozent TEXT,
        zeiten TEXT,
        sprache TEXT,
                   
        FOREIGN KEY (modul_id) REFERENCES modul(modul_id)
    )
    """) 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS abgabe (
        abgabe_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        kurs_id INTEGER NOT NULL,
        username TEXT NOT NULL,
        zeitpunkt DATETIME DEFAULT CURRENT_TIMESTAMP,
                   
        FOREIGN KEY (kurs_id) REFERENCES kursangebot(kurs_id),
        FOREIGN KEY (username) REFERENCES student(username)
    )
    """) 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS anfrage (
        anfrage_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        kurs_id INTEGER NOT NULL,
        username TEXT NOT NULL,
        zeitpunkt DATETIME DEFAULT CURRENT_TIMESTAMP,
                   
        FOREIGN KEY (kurs_id) REFERENCES kursangebot(kurs_id),
        FOREIGN KEY (username) REFERENCES student(username)
    )
    """) 
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tausch (
        tausch_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        anfrage_id INTEGER NOT NULL,
        abgabe_id INTEGER NOT NULL,
                   
        FOREIGN KEY (anfrage_id) REFERENCES anfrage(anfrage_id),
        FOREIGN KEY (abgabe_id) REFERENCES abgabe(abgabe_id)
    )
    """) 


conn.commit()

