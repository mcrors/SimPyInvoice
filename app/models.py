from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from app import db


class User(db.Model):
    username = db.Column()
    email = db.Column()
