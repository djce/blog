from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.json import JSONEncoder as _JSONEncoder
from datetime import datetime, date
import decimal
import uuid

db = SQLAlchemy()

login_manager = LoginManager()

class JSONEncoder(_JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, uuid.UUID):
            return str(o)
        elif isinstance(o, bytes):
            return o.decode('utf-8')
        else:
            _JSONEncoder.default(self, o)