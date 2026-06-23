from flask import *
from flask_login import login_required
from db_update import *
from studienburo import *
from login_blueprint import login_blueprint

app = Flask(__name__)
app.register_blueprint(sb)

app.register_blueprint(login_blueprint)
app.config["SECRET_KEY"] = "schlüssel"

DB_PATH = 'tauschdaten.db'

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")


@app.route("/verwaltung")
def verwaltung():
    return render_template("verwaltung.html")

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(401)
def internal_server_error(e):
    return render_template('401.html'), 401

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)