from flask import *
from login import app as login
from flask_login import login_required
from csv_upload import csv_page
from db_update import *
from csv_upload import *

app = Flask(__name__)
app.register_blueprint(csv_page)
app.config["SECRET_KEY"] = "schlüssel"

DB_PATH = 'tauschdaten.db'

@app.route("/")
def startapp():
    return render_template("dashboard.html")

# muss im app module sein sonnst klappt upload nicht!
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

    return render_template("csv_upload.html", form=form)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)