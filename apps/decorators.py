from flask import flash, redirect, url_for
from flask_login import current_user
from functools import wraps
from flask import g, request, session

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return wrap

#check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('home'))
    return wrap

def admin_required(func):
    """
    Modified login_required decorator to restrict access to admin group.
    """
    # zero means admin, one and up are other groups
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.role != 'admin':        
            flash("You don't have permission to access this resource.", "warning")
            return redirect(url_for("main.home"))
        return func(*args, **kwargs)
    return wrap