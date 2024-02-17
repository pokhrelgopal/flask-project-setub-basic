from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
from app import routes


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.secret_key = os.getenv("SECRET_KEY")


with app.app_context():
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    from app import models

    db.create_all()
    db.session.commit()

migrate = Migrate(app, db)
