import sqlite3

DB_PATH = 'tauschdaten.db'

def dbcon():
    connection = sqlite3.connect(DB_PATH)
    return connection

def clear_kurse():
    with dbcon() as connection:
        c = connection.cursor()

        c.execute("Delete from abgabe")
        c.execute("Delete from anfrage")
        c.execute("Delete from tausch")
        connection.commit()
        c.close()
    print("Abgaben,Anfragen und Tausche aus DB geleert!")

if __name__ == "__main__":
    clear_kurse()