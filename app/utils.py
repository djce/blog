from flask.json import JSONEncoder as _JSONEncoder
from datetime import datetime, date

class JSONEncoder(_JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            _JSONEncoder.default(self, obj)
