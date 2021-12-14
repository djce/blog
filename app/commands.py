from flask import Flask
from .auth.models import User
import click

def init_cmd(app: Flask, db):

    @app.cli.command('initdb')
    @click.option('--drop', is_flag=True, help='drop database')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('drop tables')
        db.create_all()
        click.echo('Initialized database')

    @app.cli.command('create_user')
    # @click.argument('name')
    def create_user():
        data = {}
        data['username'] = input('请输入用户名：')
        data['email'] = input('请输入邮箱：')
        data['password'] = input('请输入密码：')
        confirm_password = input('请再次输入密码：')
        if data['password'] == confirm_password:
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            click.echo('创建成功')
            return None
        click.echo('两次密码不一致!')
        

