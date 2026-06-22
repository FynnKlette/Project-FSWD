import sqlite3
from flask import Flask

app = Flask(__name__)

DB_PATH = "../tauschdaten.db"  # eine Ebene höher, im Repo-Root


@app.route("/abgaben")
def abgaben_liste():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT abgabe.abgabe_id, kursangebot.kursbezeichnung, abgabe.username, abgabe.zeitpunkt
        FROM abgabe
        JOIN kursangebot ON abgabe.kurs_id = kursangebot.kurs_id
    """)
    abgaben = cursor.fetchall()
    conn.close()

    # Vorerst als Text ausgeben — Templates kommen in Etappe 5
    ausgabe = "<h1>Abgaben</h1><ul>"
    for a in abgaben:
        ausgabe += f"<li>#{a[0]}: {a[1]} (von {a[2]}, am {a[3]})</li>"
    ausgabe += "</ul>"
    return ausgabe


if __name__ == "__main__":
    app.run(debug=True, port=5002)