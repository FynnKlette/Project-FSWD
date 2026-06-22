from flask import Flask

app = Flask(__name__)


@app.route("/show")
def studbuero():
    return render_template("show.html")

