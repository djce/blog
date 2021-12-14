from pathlib import Path
from flask import Flask
from logging.handlers import TimedRotatingFileHandler
import logging
import sys
from conf import load_config
from .auth.models import User, Role
from .posts import Post
from .extensions import db, login_manager
from .extensions import JSONEncoder
from .commands import init_cmd

BASE_DIR = Path(__file__).resolve().parent.parent
if BASE_DIR not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

def create_app():

    app = Flask(__name__, 
                template_folder=(BASE_DIR / 'templates'),
                static_folder=(BASE_DIR / 'static'))

    app.json_encoder = JSONEncoder

    app.config.from_object(load_config())

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    register_extensions(app)

    from . import routers
    routers.init_app(app)

    init_cmd(app, db)

    app.add_url_rule('/','user.home')

    return app

def register_extensions(app: Flask) -> None:

    db.init_app(app)
    db.app = app

    with app.app_context():
        db.drop_all()
        db.create_all()

    login_manager.init_app(app)

def register_log(app: Flask):
    fmt = logging.Formatter(
        '%(asctime)s | %(levelname)s  | %(module)s:<%(funcName)s>:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    # handler = RotatingFileHandler(BASE_DIR / 'logs/info.log',
    #                               maxBytes=5 * 1024 * 1024,
    #                               backupCount=10)
    handler = TimedRotatingFileHandler(
        BASE_DIR / 'logs/info.log',
        when='D', 
        interval=1, 
        backupCount=10,
        delay=True)
    handler.setFormatter(fmt)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)



