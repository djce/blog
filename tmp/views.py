# from flask import Flask,render_template,flash,redirect,url_for,request
# from flask import Blueprint,current_app,abort
# from PIL import Image
# from app.forms import RegisterationForm,LoginForm,UpdateAccountForm,PostForm,RequestResetForm,ResetPasswordForm
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user,current_user,logout_user,login_required
# from app.models import User,db,Post
# import uuid
# import secrets,os

# bp = Blueprint('bp',__name__)



# @bp.route('/home/',methods=['GET','POST'])
# def home():
#     page = request.args.get('page',1,type=int)
#     posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=2)
#     return render_template('home.html',posts=posts)


# @bp.route('/about/',methods=['GET'])
# def about():
#     return render_template('about.html')


# @bp.route('/register/',methods=['GET','POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('bp.home'))
#     form = RegisterationForm()
#     if form.validate_on_submit():
#         pw_hash = generate_password_hash(form.password.data).decode('utf-8')
#         user = User(id=get_uuid(),username=form.username.data,email=form.email.data,password=pw_hash)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Account create for {form.username.data}!','success')
#         return redirect(url_for('bp.login'))
#     return render_template('register.html',title='Register',form=form)

# @bp.route('/login/',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and check_password_hash(user.password,form.password.data):
#             login_user(user,remember=form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('bp.home'))
#         else:
#             flash('Login Unsuccessful. Please check email and password','danger')
#     return render_template('login.html',title='Login',form=form)

# @bp.route('/logout/')
# def logout():
#     logout_user()
#     return redirect(url_for('bp.login'))

# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _,f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(bp.root_path,'static/image',picture_fn)
#     output_size = (128,128)
#     i = Image.open(form_picture)
#     i.save(picture_path)

#     return picture_fn



# @bp.route('/account/',methods=['GET','POST'])
# @login_required
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             picture_file = save_picture(form.picture.data)
#             current_user.image_file = picture_file
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('Your account has been updated!','success')
#         return redirect(url_for('bp.account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static',filename='image/' + current_user.image_file)
#     return render_template('account.html',title='Account',image_file=image_file,form=form)

# def get_uuid():
#     return ''.join(str(uuid.uuid1()).split('-'))


# @bp.route('/post/new/',methods=['GET','POST'])
# @login_required
# def new_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(id=get_uuid(),title=form.title.data,content=form.content.data,author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post has been created!','success')
#         return redirect(url_for('bp.home'))
#     return render_template('create_post.html',title='New Post',form=form,legend='New Post')

# @bp.route('/post/<post_id>')
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html',title=post.title,post=post)


# @bp.route('/post/<post_id>/update/',methods=['GET','POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been update!','success')
#         return redirect(url_for('bp.post',post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html',title='Update Post',form=form,legend='Update Post')

# @bp.route('/post/<post_id>/delete/',methods=['GET','POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Youe post has been deleted!','success')
#     return redirect(url_for('bp.home'))


# @bp.route('/user/string:<username>')
# def user_posts(username):
#     page = request.args.get('page',1,type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = Post.query.filter_by(author=user)\
#         .order_by(Post.date_posted.desc())\
#         .paginate(page=page,per_page=2)
#     return render_template('user_posts.html',posts=posts,user=user)


# # def send_reset_email(user):
# #     token = user.get_reset_token()
# #     msg = Message('Password Reset Request',sender='yong.liu@transwarp.cn',recipients=[user.email])
# #     msg.body = ''' To resert your password,visit the following link:\
# #         {url_for('bp.rtset_token),token=token,_external=True}\

# #     If you did not make this require then simply ignore this email and no change will be made. \ '''
# #     mail.send(msg)
    
# # @bp.route('/reset_password')
# # def reset_request():
# #     if current_user.is_authenticated:
# #         return redirect(url_for('bp.home'))
# #     form = RequestResetForm()
# #     if form.validate_on_submit():
# #         user = User.query.filter_by(email=form.email.data).first()
# #         send_reset_email()
# #         flash('An email has been sent with instustions to reset your poassword.','info')
# #         return redirect(url_for('bp.login'))
# #     return render_template('reset_request.html',title='Reset Password',form=form)


# # @bp.route('/reset_password/<token>')
# # def reset_token(token):
# #     if current_user.is_authenticated:
# #         return redirect(url_for('bp.home'))
# #     user = User.verify_reset_token(token)
# #     if user is None:
# #         flash('That is an invalid or expired token','warning')
# #         return redirect(url_for('bp.reset_request'))
# #     form = ResetPasswordForm()
# #     if form.validate_on_submit():
# #         pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
# #         user.password = pw_hash
# #         db.session.commit()
# #         flash(f'Your password has been update!','success')
# #         return redirect(url_for('bp.login'))
# #     return render_template('reset_token.html',title='Rest Password',form=form)