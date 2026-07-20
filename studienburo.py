from flask import Blueprint, jsonify, redirect, request, url_for
from flask import render_template
from flask_wtf import FlaskForm
from flask_wtf.file import *
from wtforms import *
from db_update import *
from studburo_req import studienburo_required

DB_PATH = 'tauschdaten.db'

studienburo = Blueprint("studienburo", __name__)

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

def alle_tausche():
    with dbcon() as connection:
        c = connection.cursor()
        c.execute("""
        SELECT t.tausch_id, anfr.anfrage_id, anfr.username, anfr_stu.matrikelnummer,
                abg.abgabe_id, abg.username, abg_stu.matrikelnummer,
                k.kurs_id, k.kursbezeichnung, k.semester, k.dozent, k.sprache,
                t.status
                FROM tausch t
                JOIN anfrage anfr ON t.anfrage_id = anfr.anfrage_id
                JOIN abgabe abg ON t.abgabe_id = abg.abgabe_id
                JOIN studenten anfr_stu ON anfr.username = anfr_stu.username
                JOIN studenten abg_stu ON abg.username = abg_stu.username
                JOIN kursangebot k ON anfr.kurs_id = k.kurs_id
                ORDER BY t.tausch_id ASC
        """)
        alle_tausche = c.fetchall()
        c.close()
    return alle_tausche

@studienburo.route("/kurse", methods=['Get'])
@studienburo_required
def kurse():
    return render_template("kurse.html", kurse=alle_kurse())

@studienburo.route("/module", methods=['Get'])
@studienburo_required
def module():
    return render_template("module.html", module=alle_module())

@studienburo.route("/tauschverwaltung", methods=['Get'])
@studienburo_required
def tausche():
    # print(alle_tausche()) 
    return render_template("tauschverwaltung.html", tausche=alle_tausche())

@studienburo.route("/tauschverwaltung/status/<int:tausch_id>", methods=['Post'])
@studienburo_required
def tausch_status(tausch_id):
    status = request.form["status"]
    with dbcon() as connection:
            c = connection.cursor()
            c.execute("""
            UPDATE tausch
            SET status = ?
            WHERE tausch_id = ?
            """,(status, tausch_id))

            c.close()
            connection.commit()
    return redirect(url_for("studienburo.tausche"))
            


