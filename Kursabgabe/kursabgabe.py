from flask import Flask

app = Flask(__name__)


@app.route("/abgaben")
def abgaben_liste():
    return "Hier kommen später alle Kurs-Abgaben"


if __name__ == "__main__":
    app.run(debug=True, port=5002)