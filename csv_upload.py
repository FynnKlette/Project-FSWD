from flask import Flask, Blueprint
from flask import render_template
from flask_wtf import FlaskForm
from flask_wtf.file import *
from wtforms import *
from db_update import *

DB_PATH = 'tauschdaten.db'

csv_page = Blueprint("csv_page", __name__)

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

@csv_page.route("/kurse", methods=['Get'])
def kurse():
    return render_template("kurse.html", kurse=alle_kurse())

@csv_page.route("/module", methods=['Get'])
def module():
    return render_template("module.html", module=alle_module())