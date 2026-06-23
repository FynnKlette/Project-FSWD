from db_update import dbcon
from db_reinigen import db_reinigen

DB_PATH = 'tauschdaten.db'

def tausche_eintragen(passendetausche_liste):
    eintrage_erfolgt = 0
    with dbcon() as connection:
        c = connection.cursor()

        for eintrag in passendetausche_liste:
            try:
                c.execute("""
                INSERT INTO tausch (anfrage_id, abgabe_id) 
                VALUES (?, ?)
                """, (eintrag[0],eintrag[1]))
                eintrage_erfolgt += 1
            except:
                print(f"Fehler beim Einfügen in Datenbank: {eintrag}")

        connection.commit()
        c.close()
        return eintrage_erfolgt

def globale_tauschfindung():

    db_reinigen()

    patner_gematched_anzahl = 0

    with dbcon() as connection:
        c = connection.cursor()

         #sql für offene anfragen
        c.execute("""
        SELECT anfrage_id, username, min(zeitpunkt) as erste_zeit, kurs_id
        FROM anfrage
        WHERE anfrage_id NOT IN (SELECT anfrage_id FROM tausch)
        GROUP BY kurs_id, username
        ORDER BY erste_zeit ASC
        """)
        offene_anfragen = c.fetchall()

        #sql für offene abgaben
        c.execute("""
        SELECT abgabe_id, username, min(zeitpunkt) as erste_zeit, kurs_id
        FROM abgabe
        WHERE abgabe_id NOT IN (SELECT abgabe_id FROM tausch)
        GROUP BY kurs_id, username
        ORDER BY erste_zeit ASC
        """)
        offene_abgaben = c.fetchall()
        db_offene_abgaben = offene_abgaben.copy()

        # sucht passende patner nach fifo
        passende_tausche = []
        passende_tausche_print = []

        for a in offene_anfragen:  

            for b in offene_abgaben:

                if a[3] == b[3] and a[1] != b[1]:
                    passende_tausche_print.append(f"{a[1]} + {b[1]} tauschen {a[0]}/{b[0]}!")

                    passende_anfrage_kurs_id = a[0]
                    passende_abgabe_kurs_id = b[0]
                    passende_tausche.append([passende_anfrage_kurs_id, passende_abgabe_kurs_id])
                    offene_abgaben.remove(b)
                    patner_gematched_anzahl += 1
                elif a[1] == b[1]:
                    print(f"Eigentausch nicht gestattet: {a[1]}/{b[1]}")
                else:
                    print("Fehler bei der Tauschfindung")

        connection.commit()
        c.close()

    print("-----------------------------------------------")
    # print(f"offene Abgaben: {offene_abgaben}")
    print(f"offene Abgaben: {db_offene_abgaben}")
    print(f"offene Anfragen: {offene_anfragen}")
    print(f"{patner_gematched_anzahl} passende(r) Tausch/Täusche: {passende_tausche_print}")
    print(f"passende_tausche: {passende_tausche}")
    print("-----------------------------------------------")
    tausch_eingetragen = tausche_eintragen(passende_tausche)
    print (f"{tausch_eingetragen} Täusche eingetragen in tausch tabelle")
    print("-----------------------------------------------")

if __name__ == "__main__":
    globale_tauschfindung()