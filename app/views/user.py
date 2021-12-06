from flask import Blueprint
from flask import render_template
from flask import flash
from flask import jsonify, Response
from flask import request,session
import json

from app.utils import JSONEncoder

from collections import OrderedDict


from flask import redirect,url_for

from flask_login import login_user,current_user, logout_user

from sqlalchemy import or_,and_

from datetime import datetime

from ..models import User
from ..forms.user import LoginForm, RegistForm

from ..extensions import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/home', methods=['GET'])
def home():
    # flash('Hello world!','success')
    return render_template('index.html')


@user_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))

    if form.validate_on_submit():
        user = User.query.filter(or_(User.email == form.username.data, User.username == form.username.data)).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=form.remember.data)
            user.last_login = datetime.now().__format__('%Y-%m-%d %H:%M:%S')
            db.session.commit()
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('user.home'))
    return render_template('admin/login.html', form=form)

@user_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))

@user_bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))

    form = RegistForm()

    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.login'))
    return render_template('admin/register.html', title='注册', form=form)

@user_bp.route('/user')
def get_users():
    users = User.query.all()
    data = [ OrderedDict(user.to_dict()) for user in users if user is not None]
    print(data)

    # return jsonify({'code': 200, 'data': data })
    return Response(json.dumps(data, cls=JSONEncoder), mimetype='application/json')
