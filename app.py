from flask import *
from login import app as login

app = Flask(__name__)


@app.route("/")
def startapp():
    return render_template("dashboard.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
