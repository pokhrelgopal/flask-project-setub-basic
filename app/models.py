from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(10), nullable=False, default="user")

    def __repr__(self):
        return "<User %r>" % self.username

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)
