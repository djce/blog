from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.validators import ValidationError

from ..models import User

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[ DataRequired() ])
    password = PasswordField('密码', validators=[ DataRequired() ])
    remember = BooleanField('记住密码')
    submit = SubmitField('登录')

class RegistForm(FlaskForm):
    username = StringField('用户名',
                            validators=[ DataRequired(), Length(min=2, max=15) ])
    email = StringField('邮箱',
                        validators=[ DataRequired(), Email() ])
    password = PasswordField('密码', validators=[ DataRequired() ])
    confirm_password = PasswordField('确认密码',
                                    validators=[ DataRequired(), EqualTo('password') ])
    submit = SubmitField('注册')

    def validate_username(self, attr):
        user = User.query.filter_by(username=attr.data).first()
        if user:
            raise ValidationError(f'Username {attr.data} is not available. Please choose another.')
    
    def validate_email(self, attr):
        user = User.query.filter_by(email=attr.data).first()
        if user:
            raise ValidationError(f'Email {attr.data} is not available. Please choose another.')
