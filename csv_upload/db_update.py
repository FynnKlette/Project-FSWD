import sqlite3
import io
import csv

DB_PATH = '../tauschdaten.db'

def dbcon():
    connection = sqlite3.connect(DB_PATH)
    return connection

def clear_kurse():
    with dbcon() as connection:
        c = connection.cursor()

        c.execute("Delete from kursangebot")
        c.execute("Delete from modulzuordnung")
        c.execute("Delete from modul")
        connection.commit()
        c.close()
    print("Kurse/Module aus DB geleert!")

def csv_in_list(csv_data_str):

    stream = io.StringIO(csv_data_str, newline=None)
    csv_reader = csv.reader(stream, delimiter=",")

    csv_list = []

    for row in csv_reader:
        csv_list.append(row)
    return csv_list

def update_kurse(csv_list):

    clear_kurse()

    liste = csv_list[1:]

    with dbcon() as connection:
        c = connection.cursor()

        i = 0

        for spalte in liste:
            if not spalte or len(spalte) == 0:
                continue
            try:
                # Angebotsnummer,Bezeichnung,Credits,Prüfungsvorlage,Veranstaltungstyp,Dozierende,Sprache
                # 0,                1,          2,      3,              4,              5,          6
                modul_id = spalte[0]
                modulbezeichnung = spalte[1]
                etcs = spalte[2]
                sws = "nicht angegeben"
                pruefungsform = spalte[3]
                zeiten = spalte[4]
                semester = "SoSe26"
                dozent = spalte[5]
                sprache = spalte[6]
                studiengang = "nicht angegeben"

            except IndexError:
                print("Fehler bei Spalten")
                continue

            #modul
            c.execute("""
                INSERT OR IGNORE INTO modul (modul_id, modulbezeichnung, etcs, sws, prüfungsform) 
                VALUES (?, ?, ?, ?, ?)
            """, (modul_id, modulbezeichnung, etcs, sws, pruefungsform))

            #kurse
            c.execute("""
                INSERT INTO kursangebot (kursbezeichnung, modul_id, semester, dozent, zeiten, sprache) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (modulbezeichnung, modul_id, semester, dozent, zeiten, sprache))

            #kurszuordnung
            c.execute("""
                INSERT INTO modulzuordnung (modul_id, studiengang) 
                VALUES (?, ?)
            """, (modul_id, studiengang))

            i += 1

        connection.commit()
        c.close()
        print(f"Erfolgreich geändert: {i}Kurse hinzugefügt")
        return f"{i} Kurse erneuert!"
                
            
                


