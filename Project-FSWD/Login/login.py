from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def login_seite():
    return render_template("show.html")


@app.route("/anmelden", methods=["POST"])
def anmelden():

    email = request.form("email")
    password = request.form("password") 

    if not email.endswith("@stud.hwr-berlin.de"):
        return "Fehler: Nur HWR-E-Mails erlaubt"

    if len(password) < 6:
        return "Fehler: Passwort muss mindestens 6 Zeichen haben"

    if len(password) > 15:
        return "Fehler: Passwort darf maximal 15 Zeichen haben"

    return "Eingaben sind gültig"

@app.route("/registrieren")
def registrieren():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
