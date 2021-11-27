from pathlib import Path
from flask import Flask
from conf import load_config
from .models import *
from .extensions import db, login_manager
from .commands import init_cmd

BASE_DIR = Path(__file__).resolve().parent.parent

def create_app():

    app = Flask(__name__, 
                template_folder=(BASE_DIR / 'templates'),
                static_folder=(BASE_DIR / 'static'))

    app.config.from_object(load_config())\

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    register_extensions(app)

    from . import views
    views.init_app(app)

    init_cmd(app, db)

    app.add_url_rule('/','user.home')

    return app

def register_extensions(app: Flask) -> None:

    db.init_app(app)
    db.app = app
    db.create_all()

    login_manager.init_app(app)



