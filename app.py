from flask import *
from login import app as login

app = Flask(__name__)


@app.route("/")
def startapp():
    return render_template("dashboard.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
from flask import Flask, render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(401)
def internal_server_error(e):
    return render_template('401.html'), 401