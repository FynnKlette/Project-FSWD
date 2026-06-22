from flask import *

app = Flask(__name__)


@app.route("/")
def startapp():
    return render_template("show.html")

