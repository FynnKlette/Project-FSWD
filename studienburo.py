from flask import Blueprint
from flask import render_template
from flask_wtf import FlaskForm
from flask_wtf.file import *
from wtforms import *
from db_update import *

DB_PATH = 'tauschdaten.db'

sb = Blueprint("studienburo", __name__)

class UploadForm(FlaskForm):
    upload_input = FileField("CSV Hochladen",validators=[FileAllowed(['csv']), FileRequired()])
    submit = SubmitField("Hochladen")

def alle_kurse():
    with dbcon() as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM kursangebot")
        alle_kurse = c.fetchall()
        c.close()
    return alle_kurse

def alle_module():
    with dbcon() as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM modul")
        alle_module = c.fetchall()
        c.close()
    return alle_module

def tauschdaten():
    with dbcon() as connection:
        c = connection.cursor()
        c.execute("""
        SELECT t.tausch_id, 
        t.anfrage_id, saf.vorname, saf.name, saf.matrikelnummer, 
        t.abgabe_id, sab.vorname, sab.name, sab.matrikelnummer, 
        k.kurs_id, k.kursbezeichnung, k.semester, k.dozent, k.sprache FROM tausch t
        JOIN anfrage af ON t.anfrage_id = af.anfrage_id 
        JOIN abgabe ab ON t.abgabe_id = ab.abgabe_id 
        JOIN kursangebot k ON ab.kurs_id = k.kurs_id
        JOIN studenten sab ON ab.username = sab.username
        JOIN studenten saf ON af.username = saf.username
        """)
        tdaten = c.fetchall()
        c.close()
        print(tdaten)
    return tdaten

@sb.route("/kurse", methods=['Get'])
def kurse():
    return render_template("kurse.html", kurse=alle_kurse())

@sb.route("/module", methods=['Get'])
def module():
    return render_template("module.html", module=alle_module())

@sb.route("/tauschverwaltung", methods=['Get'])
def tauschverwaltung():
    return render_template("tauschverwaltung.html", tauschdaten=tauschdaten())