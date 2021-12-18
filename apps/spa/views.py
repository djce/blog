from flask import Blueprint
from flask import render_template

spa_bp = Blueprint('spa', __name__)

@spa_bp.route('/', methods=['GET'])
def spa():
    return render_template('spa/index.html')


@spa_bp.route('/home', methods=['GET'])
def home():
    return render_template('spa/home.html')

@spa_bp.route('/about', methods=['GET'])
def about():
    return render_template('spa/about.html')

@spa_bp.route('/contact', methods=['GET'])
def contact():
    return render_template('spa/contact.html')