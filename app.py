from flask import *
from login import app as login
from csv_upload import csv_page

app = Flask(__name__)
app.register_blueprint(csv_page)
app.config["SECRET_KEY"] = "schlüssel"

DB_PATH = 'tauschdaten.db'

@app.route("/")
def startapp():
    return render_template("dashboard.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
