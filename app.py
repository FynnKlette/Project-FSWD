from flask import *
from flask_login import login_required, UserMixin, LoginManager
from studienburo import studienburo
from db_update import *
from studienburo import *
from loginbp import login_blueprint
from studburo_req import studienburo_required

app = Flask(__name__)
app.register_blueprint(studienburo)
app.register_blueprint(login_blueprint)
app.config["SECRET_KEY"] = "schlüssel"

DB_PATH = 'tauschdaten.db'


login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_blueprint.login_seite" # Umleitung, falls nicht eingelogt

class User(UserMixin):
    def __init__(self,id):
        self.id=id


#user erkennen
@login_manager.user_loader
def load_user(user_id):
    if not user_id:
        return None
    return User(user_id)



@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/verwaltung")
@login_required
def verwaltung():
    if "mitarbeiter" not in session:
        flash ("Zugriff verweigert", "zugriff_nichtig")
        return render_template("show.html")
    return render_template("verwaltung.html")


# muss im app module sein sonnst klappt upload nicht!
@app.route("/upload_csv", methods=['Get', 'Post'])
@login_required
@studienburo_required
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
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(401)
def unauthorized_error(e):
    return render_template('401.html'), 401

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)