from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import orm
from ..extensions import db, login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

db.Table(
    'tbl_auth_user_roles',
    db.Column('id', db.Integer, autoincrement=True, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('tbl_auth_user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('tbl_auth_role.id'))
)

class User(db.Model, UserMixin):
    __tablename__ = 'tbl_auth_user'
    id = db.Column( db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(200), default='avatar.png')
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    roles = db.relationship('Role', secondary='tbl_auth_user_roles',
                            backref=db.backref('users', lazy='dynamic'))
    posts = db.relationship('Post', backref='author', lazy=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # @orm.reconstructor
    # def __init__(self):
    #     pass

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self) -> str:
        return f'<User {self.username}>'

class Role(db.Model):
    __tablename__ = 'tbl_auth_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __str__(self):
        return f'<Role {self.name}>'



