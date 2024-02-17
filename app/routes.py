from flask import render_template
from app import app
from app.models import User


@app.route("/")
def index():
    return render_template("index.html")
