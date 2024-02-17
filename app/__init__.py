from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()


# ! Set up media folder
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
MEDIA_FOLDER = os.path.join(os.getcwd(), "media")
MEDIA = os.path.join("media", "uploads")

"""
If you need more folder to store media files, you can create more variables like MEDIA_FOLDER and MEDIA, with the path to the folder you want to store the media files.
"""


app = Flask(__name__)


# ! Serve media files
@app.route("/media/<path:filename>")
def media_files(filename):
    return send_from_directory(MEDIA_FOLDER, filename)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.secret_key = os.getenv("SECRET_KEY")


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes


with app.app_context():
    db.create_all()
