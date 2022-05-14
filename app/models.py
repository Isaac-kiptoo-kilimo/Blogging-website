
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from . import db
from datetime import datetime


class Blog:
    def __init__(self,author,id,quote,permalink):
        self.author=author
        self.id=id
        self.quote=quote
        self.permalink="http://quotes.stormconsultancy.co.uk/quotes/1" + permalink



class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,)
    username=db.Column(db.string(255),unique=True,nullable=False)
    fullname=db.Column(db.string(255),index=True,nullable=False)
    email=db.Column(db.string(255),unique=True,index=True,nullable=False)
    bio=db.Column(db.string(255),nullable=False)
    password_secure=db.Column(db.string(255),nullable=False)
    active = db.Column(db.Boolean(), default=True)
    admin = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    quotes = db.relationship('Quote', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
      return self.fullname

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

class Quote(db.Model):
    __tablename__='quotes'
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    title=db.Column(db.string(255),nullable=False)
    author=db.Column(db.string(255),nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    downvotes = db.Column(db.Integer, default=0)
    upvotes = db.Column(db.Integer, default=0)

    def __repr__(self):
      return self.title


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
      return self.content

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    quotes = db.relationship('Quote', backref='category', lazy=True)

    def __repr__(self):
        return self.name
