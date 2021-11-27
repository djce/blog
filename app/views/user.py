from flask import Blueprint
from flask import render_template
from flask import flash
from flask import jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/index', methods=['GET'])
def home():
    # flash('Hello world!','success')
    return render_template('home.html')