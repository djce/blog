from flask import Flask
from flask import current_app
from flask_login import LoginManager
import os

def create_app():

    app = Flask(__name__)
    app.config['ENV'] = 'development'
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(app.instance_path,'site.sqlite3'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '7f66dfc8b92fa4dda06761a11b097734'
    # app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.models import db,User,Post,ma
    db.app = app
    db.init_app(app)

    ma.app = app
    ma.init_app(app)

    db.create_all()

    from app.models import login_manager
    login_manager.init_app(app)

    from app.views import bcrypt
    bcrypt.init_app(app)

    # from app.views import mail
    # mail.init_app(app)

    from app.api.v1.user import api
    app.register_blueprint(api,url_prefix='/v1')

    from app.views import bp
    app.register_blueprint(bp)

    app.add_url_rule('/','bp.login')

    return app
