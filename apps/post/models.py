from datetime import datetime
from ..extensions import db

class Post(db.Model):
    __tablename__ = 'tbl_blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_auth_user.id'), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return f'<Post {self.title}>'

class Category(db.Model):
    __tablename__ = 'tbl_blog_category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('tbl_blog_category.id'))

    def __str__(self):
        return f'<Category {self.title}>'


class Comment(db.Model):
    __tablename__ = 'tbl_blog_comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    post_id = db.Column(db.Integer, db.ForeignKey('tbl_blog_post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_auth_user.id'), nullable=False)

class Reply(db.Model):
    __tablename__ = 'tbl_blog_reply'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    type = db.Column(db.String(10))
    comment_id = db.Column(db.Integer, db.ForeignKey('tbl_blog_comment.id'), nullable=False)
    reply_id = db.Column(db.Integer, db.ForeignKey('tbl_blog_reply.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('tbl_blog_reply.id'), nullable=False)
    origin_id = db.Column(db.Integer, db.ForeignKey('tbl_auth_user.id'), nullable=False)