from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.validators import ValidationError

from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[ DataRequired() ])
    password = PasswordField('Password', validators=[ DataRequired() ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistForm(FlaskForm):
    username = StringField('Username',
                            validators=[ DataRequired(), Length(min=2, max=15) ])
    email = StringField('Email',
                        validators=[ DataRequired(), Email() ])
    password = PasswordField('Password', validators=[ DataRequired() ])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[ DataRequired(), EqualTo('password') ])
    submit = SubmitField('Sign Up')

    def validate_username(self, attr):
        user = User.query.filter_by(username=attr.data).first()
        if user:
            raise ValidationError(f'Username {attr.data} is not available. Please choose another.')
    
    def validate_email(self, attr):
        user = User.query.filter_by(email=attr.data).first()
        if user:
            raise ValidationError(f'Email {attr.data} is not available. Please choose another.')
