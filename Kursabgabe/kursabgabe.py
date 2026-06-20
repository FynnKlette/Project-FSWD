import sqlite3
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "asem-dev-key-2026"

DB_PATH = "../tauschdaten.db"  # eine Ebene höher, im Repo-Root

class AbgabeForm(FlaskForm):
    kurs = SelectField(
        "Kurs",
        choices=[],         # füllen in Route dynamisch aus der DB
        coerce=int,
        validators=[DataRequired()]
    )
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Abgabe speichern")

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

    # Vorerst als Text ausgeben — 
    ausgabe = "<h1>Abgaben</h1><ul>"
    for a in abgaben:
        ausgabe += f"<li>#{a[0]}: {a[1]} (von {a[2]}, am {a[3]})</li>"
    ausgabe += "</ul>"
    return ausgabe

@app.route("/abgaben/neu")
def abgabe_neu():
    # Kurse aus DB holen für das Dropdown
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT kurs_id, kursbezeichnung FROM kursangebot")
    kurse = cursor.fetchall()
    conn.close()

    # Form-Objekt erstellen und Choices setzen
    form = AbgabeForm()
    form.kurs.choices = kurse   # [(1, 'Marketing SoSe26'), (2, ...), ...]

    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5002)