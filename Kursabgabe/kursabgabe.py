import sqlite3
from flask import Flask, render_template, redirect, url_for, flash
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
        ORDER BY abgabe.zeitpunkt ASC
    """)
    abgaben = cursor.fetchall()
    conn.close()

    return render_template("liste.html", abgaben=abgaben)

@app.route("/abgaben/neu", methods=["GET", "POST"])
def abgabe_neu():
    # Kurse aus DB holen für das Dropdown
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT kurs_id, kursbezeichnung FROM kursangebot")
    kurse = cursor.fetchall()

    # Form-Objekt erstellen und Choices setzen
    form = AbgabeForm()
    form.kurs.choices = kurse

    # POST: Wenn das Formular abgesendet und gültig ist
    if form.validate_on_submit():
        cursor.execute(
            "INSERT INTO abgabe (kurs_id, username) VALUES (?, ?)",
            (form.kurs.data, form.username.data)
        )
        conn.commit()
        conn.close()
        flash("Abgabe erfolgreich gespeichert!", "success")
        return redirect(url_for("abgaben_liste"))

    conn.close()
    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5002)