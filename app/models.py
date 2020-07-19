from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager,UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    id = db.Column(db.String(32),primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(20),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

    def get_reset_token(self,expires_sec=1800):
        s = Serializer(current_app.config['SERRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SERRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
      
    def __repr__(self):
        return f"User('{self.username}"

class Post(db.Model):
    id = db.Column(db.String(32),primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.String(32),db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}"

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email','image_file')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
