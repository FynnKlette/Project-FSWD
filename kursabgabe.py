import sqlite3
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "asem-dev-key-2026"

DB_PATH = "tauschdaten.db"


class AbgabeForm(FlaskForm):
    kurs = SelectField(
        "Kurs",
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Abgabe speichern")


class AnfrageForm(FlaskForm):
    kurs = SelectField(
        "Kurs",
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Anfrage speichern")


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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT kurs_id, kursbezeichnung FROM kursangebot")
    kurse = cursor.fetchall()

    form = AbgabeForm()
    form.kurs.choices = kurse

    if form.validate_on_submit():
        # Prüfen, ob der Username in der studenten-Tabelle existiert
        cursor.execute(
            "SELECT username FROM studenten WHERE username = ?",
            (form.username.data,)
        )
        student = cursor.fetchone()

        if student is None:
            conn.close()
            flash("Username existiert nicht. Bitte zuerst registrieren!", "error")
            return redirect(url_for("abgabe_neu"))

        # Prüfen, ob dieser User für diesen Kurs schon eine Abgabe hat
        cursor.execute(
            "SELECT abgabe_id FROM abgabe WHERE username = ? AND kurs_id = ?",
            (form.username.data, form.kurs.data)
        )
        existierende_abgabe = cursor.fetchone()

        if existierende_abgabe is not None:
            conn.close()
            flash("Du hast diesen Kurs bereits zur Abgabe eingestellt!", "error")
            return redirect(url_for("abgabe_neu"))

        # Alles OK → Abgabe speichern
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


@app.route("/anfragen")
def anfragen_liste():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT anfrage.anfrage_id, kursangebot.kursbezeichnung, anfrage.username, anfrage.zeitpunkt
        FROM anfrage
        JOIN kursangebot ON anfrage.kurs_id = kursangebot.kurs_id
        ORDER BY anfrage.zeitpunkt ASC
    """)
    anfragen = cursor.fetchall()
    conn.close()

    return render_template("anfrage_liste.html", anfragen=anfragen)


@app.route("/anfragen/neu", methods=["GET", "POST"])
def anfrage_neu():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT kurs_id, kursbezeichnung FROM kursangebot")
    kurse = cursor.fetchall()

    form = AnfrageForm()
    form.kurs.choices = kurse

    if form.validate_on_submit():
        # Prüfen, ob der Username existiert
        cursor.execute(
            "SELECT username FROM studenten WHERE username = ?",
            (form.username.data,)
        )
        student = cursor.fetchone()

        if student is None:
            conn.close()
            flash("Username existiert nicht. Bitte zuerst registrieren!", "error")
            return redirect(url_for("anfrage_neu"))

        # Prüfen, ob dieser User für diesen Kurs schon eine Anfrage hat
        cursor.execute(
            "SELECT anfrage_id FROM anfrage WHERE username = ? AND kurs_id = ?",
            (form.username.data, form.kurs.data)
        )
        existierende_anfrage = cursor.fetchone()

        if existierende_anfrage is not None:
            conn.close()
            flash("Du hast diesen Kurs bereits angefragt!", "error")
            return redirect(url_for("anfrage_neu"))

        # Alles OK → Anfrage speichern
        cursor.execute(
            "INSERT INTO anfrage (kurs_id, username) VALUES (?, ?)",
            (form.kurs.data, form.username.data)
        )
        conn.commit()
        conn.close()
        flash("Anfrage erfolgreich gespeichert!", "success")
        return redirect(url_for("anfragen_liste"))

    conn.close()
    return render_template("anfrage_form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5002)