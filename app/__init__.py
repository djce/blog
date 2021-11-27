from flask import Flask
from flask import current_app

import os

def create_app():

    app = Flask(__name__)

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass





    # app.add_url_rule('/','bp.login')

    return app


def init_extensions(app: Flask) -> None:

    from .extensions import db, login_manager

    db.init_app(app)
    db.app = app
    db.create_all()

    login_manager.init_app(app)
