from flask import render_template,url_for,redirect,flash,request

from .forms import RegistrationForm,LoginForm
from flask_login import login_user,login_required,logout_user
from app.models import  User
from app import db
# from ..email import mail_message
from . import auth



@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "watchlist login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    user_exist=User.query.filter_by(email=form.email.data).first() 
    if request.method=='POST':

        if form.validate_on_submit() and user_exist is None: 
    
            user = User(username=form.username.data, email=form.email.data,password=form.password.data)

            print(form.username)
            db.session.add(user)
            db.session.commit()
            
            # mail_message("Welcome to Movie of the day","email/welcome_user",user.email,user=user)
            flash('Yaaaay! Thanks for registering!')

            return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html',title='signup',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
