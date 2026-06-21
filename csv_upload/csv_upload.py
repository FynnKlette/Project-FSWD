from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from flask_wtf.file import *
from wtforms import *
from db_update import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "schlüssel"

class UploadForm(FlaskForm):
    upload_input = FileField("CSV Hochladen",validators=[FileAllowed(['csv']), FileRequired()])
    submit = SubmitField("Hochladen")

@app.route("/upload_csv", methods=['Get', 'Post'])
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

    else: render_template("fehler.html")

    return render_template("csv_upload.html", form=form)

@app.route("/kurse", methods=['Get'])
def kurse():
    return "hier werden die kurse in db angezeigt"

if __name__ == "__main__":
    app.run(debug=True, port=5003)