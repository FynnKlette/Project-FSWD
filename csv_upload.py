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

@csv_page.route("/upload_csv", methods=['Get', 'Post'])
def upload_csv():
    form = UploadForm()

    if form.validate_on_submit():
        file = form.upload_input.data
        csv_data = file.stream.read().decode("utf-8")
        liste = csv_in_list(csv_data)
        print(liste)
        print(len(liste))
        i = update_kurse(liste)
        return render_template("erfolgreich.html", anzahl=i)

    return render_template("csv_upload.html", form=form)

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