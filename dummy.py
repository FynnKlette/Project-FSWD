from db_update import dbcon
import sqlite3
import time

DB_PATH = 'tauschdaten.db'

# immer nur vorhandene username und kurs_id nutzen 

def create_abgabe_dummy(kurs_id,username):

    with dbcon() as connection:
        c = connection.cursor()

        c.execute("""
                INSERT OR IGNORE INTO abgabe (kurs_id, username) 
                VALUES (?, ?)
            """, (kurs_id,username))
        
        connection.commit()
        c.close()
        print(f"Abgabe Erstellt: {username}, {str(kurs_id)}")


def create_anfrage_dummy(kurs_id,username):

    with dbcon() as connection:
        c = connection.cursor()

        c.execute("""
                INSERT OR IGNORE INTO anfrage (kurs_id, username) 
                VALUES (?, ?)
            """, (kurs_id,username))
        
        connection.commit()
        print(f"Anfrage Erstellt: {username}, {str(kurs_id)}")

def leere_anfrage_abgabe():
        with dbcon() as connection:
            c = connection.cursor()

            c.execute("Delete from anfrage")
            print("Anfrage tabelle geleert")

            c.execute("Delete from abgabe")
            print("Abgabe tabelle geleert")

            connection.commit()
            c.close()

def leere_tausche():
        with dbcon() as connection:
            c = connection.cursor()

            c.execute("Delete from tausch")
            print("Tausch tabelle geleert")

            connection.commit()
            c.close()

leere_anfrage_abgabe()
leere_tausche()

create_abgabe_dummy(1174, "TestUser")
time.sleep(0.01)
create_abgabe_dummy(1174, "TestUser")
create_abgabe_dummy(1174, "TestUser")
create_abgabe_dummy(1174, "TestUser")
create_abgabe_dummy(1174, "TestUser")

# time.sleep(0.01)
# create_abgabe_dummy(1174, "TestUser123")

create_anfrage_dummy(1174, "Dan")
time.sleep(0.01)
create_anfrage_dummy(1174, "Ben")
create_anfrage_dummy(1174, "Ben")
create_anfrage_dummy(1174, "Ben")

