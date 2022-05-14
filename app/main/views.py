from flask import render_template,request,redirect,url_for, flash
from ..requests import get_blogs
from . import main
from .. import db, login_manager
from ..models import User,Comment, Category

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    quotes = get_blogs()
    
    users=User.query.all()
    print('users',users)
    return render_template ("pages/index.html",quotes=quotes)

@main.route('/blogs/add')
def addblog():
    return render_template ('pages/blogs/addblog.html')