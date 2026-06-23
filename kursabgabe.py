import sqlite3
from flask import Flask, render_template, redirect, url_for, flash, Blueprint
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user

kursabgabe = Blueprint("kursabgabe", __name__)

DB_PATH = "tauschdaten.db"

class AbgabeForm(FlaskForm):
    kurs = SelectField(
        "Kurs",
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    submit = SubmitField("Abgabe speichern")


class AnfrageForm(FlaskForm):
    kurs = SelectField(
        "Kurs",
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    submit = SubmitField("Anfrage speichern")


@kursabgabe.route("/abgaben")
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


@kursabgabe.route("/abgaben/neu", methods=["GET", "POST"])
def abgabe_neu():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT kurs_id, kursbezeichnung FROM kursangebot")
    kurse = cursor.fetchall()

    form = AbgabeForm()
    form.kurs.choices = kurse

    if form.validate_on_submit():
        current_username = current_user.username
        # Prüfen, ob der Username in der studenten-Tabelle existiert
        cursor.execute(
            "SELECT username FROM studenten WHERE username = ?",
            (current_username,)
        )
        student = cursor.fetchone()

        if student is None:
            conn.close()
            flash("Username existiert nicht. Bitte zuerst registrieren!", "error")
            return redirect(url_for("kursabgabe.abgabe_neu"))

        # Prüfen, ob dieser User für diesen Kurs schon eine Abgabe hat
        cursor.execute(
            "SELECT abgabe_id FROM abgabe WHERE username = ? AND kurs_id = ?",
            (current_username, form.kurs.data)
        )
        existierende_abgabe = cursor.fetchone()

        if existierende_abgabe is not None:
            conn.close()
            flash("Du hast diesen Kurs bereits zur Abgabe eingestellt!", "error")
            return redirect(url_for("kursabgabe.abgabe_neu"))

        # Alles OK → Abgabe speichern
        cursor.execute(
            "INSERT INTO abgabe (kurs_id, username) VALUES (?, ?)",
            (form.kurs.data, current_username)
        )
        conn.commit()
        conn.close()
        flash("Abgabe erfolgreich gespeichert!", "success")
        return redirect(url_for("kursabgabe.abgaben_liste"))

    conn.close()
    return render_template("form.html", form=form)


@kursabgabe.route("/anfragen")
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


@kursabgabe.route("/anfragen/neu", methods=["GET", "POST"])
def anfrage_neu():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT kurs_id, kursbezeichnung FROM kursangebot")
    kurse = cursor.fetchall()

    form = AnfrageForm()
    form.kurs.choices = kurse

    if form.validate_on_submit():
        current_username = current_user.username
        # Prüfen, ob der Username existiert
        cursor.execute(
            "SELECT username FROM studenten WHERE username = ?",
            (current_username,)
        )
        student = cursor.fetchone()

        if student is None:
            conn.close()
            flash("Username existiert nicht. Bitte zuerst registrieren!", "error")
            return redirect(url_for("kursabgabe.anfrage_neu"))

        # Prüfen, ob dieser User für diesen Kurs schon eine Anfrage hat
        cursor.execute(
            "SELECT anfrage_id FROM anfrage WHERE username = ? AND kurs_id = ?",
            (current_username, form.kurs.data)
        )
        existierende_anfrage = cursor.fetchone()

        if existierende_anfrage is not None:
            conn.close()
            flash("Du hast diesen Kurs bereits angefragt!", "error")
            return redirect(url_for("kursabgabe.anfrage_neu"))

        # Alles OK → Anfrage speichern
        cursor.execute(
            "INSERT INTO anfrage (kurs_id, username) VALUES (?, ?)",
            (form.kurs.data, current_username)
        )
        conn.commit()
        conn.close()
        flash("Anfrage erfolgreich gespeichert!", "success")
        return redirect(url_for("kursabgabe.anfragen_liste"))

    conn.close()
    return render_template("anfrage_form.html", form=form)