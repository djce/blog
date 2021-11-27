from flask_login import UserMixin
from ..extensions import db
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    is_active = db.Column(db.Boolean, default=True)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
