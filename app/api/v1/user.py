from flask import  Blueprint
from flask import request
from flask import jsonify
from flask import Response
from flask import current_app
from app.models import *
import uuid,json

api = Blueprint('api',__name__)

# @api.route('/user/',methods=['POST'])
# def add_user():
#     id = _get_uuid()
#     user_name = request.json['user_name']
#     user_name = request.json['user_name']
#     user_name = request.json['user_name']
#     user = User(user_id,user_name)

#     db.session.add(user)
#     db.session.commit()

#     return user_schema.jsonify(user)

@api.route('/user/',methods=['GET'])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    # current_app.logger.info(result)

    return jsonify(result)

def _get_uuid():
    return ''.join(str(uuid.uuid1()).split('-'))