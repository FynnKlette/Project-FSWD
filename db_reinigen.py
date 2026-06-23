from db_update import dbcon

def db_reinigen():
    with dbcon() as connection:
        c = connection.cursor()

        # tabelle abgaben reinigen
        c.execute("""
        DELETE FROM abgabe
        WHERE abgabe_id NOT IN (SELECT MIN(abgabe_id) as min FROM abgabe GROUP BY kurs_id, username)
        """)
        abgaben_duplikate = c.rowcount

        # tabelle anfragen reinigen
        c.execute("""
        DELETE FROM anfrage
        WHERE anfrage_id NOT IN (SELECT MIN(anfrage_id) as min FROM anfrage GROUP BY kurs_id, username)
        """)
        anfragen_duplikate = c.rowcount

        connection.commit()
        c.close()
        print("-----------------------------------------------")
        print(f"{abgaben_duplikate} Abgaben-Duplikate und {anfragen_duplikate} Anfragen-Duplikate aus DB gereinigt!")

if __name__ == "__main__":
    db_reinigen()