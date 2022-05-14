from flask import render_template,request,redirect,url_for, flash
from . import main
from .. import db, login_manager
from ..models import User,Comment, Category

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    return render_template ("pages/index.html")