from flask import render_template,request,redirect,url_for, flash
from ..requests import get_blogs
from . import main
from .. import db, login_manager
from ..models import Blog, User,Comment, Category
from flask_login import login_user, current_user, logout_user, login_required


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def make_blogs(blogs):

  new_blogs = []
  for blog in blogs:
    user = User.query.filter_by(id=blog.user_id).first()
    category = Category.query.filter_by(id=blog.category_id).first()
    comments = Comment.query.filter_by(blog_id=blog.id).all()
    new_blog.append({
      'id': blog.id,
      'title': blog.title,
      'author': blog.author,
      'content': blog.content,
      'category': category,
      'user': user,
      'upvotes': blog.upvotes,
      'downvotes': blog.downvotes,
      'comments': len(comments)
    })
  return new_blogs

@main.route('/')
def index():
    quotes = get_blogs()
    
    users=User.query.all()
    print('users',users)
    return render_template ("pages/index.html",quotes=quotes)

@main.route('/blogs/add')
def addblog():
    categories = Category.query.order_by(Category.id.asc()).all()
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    new_blogs = make_blogs(blogs)
    return render_template ('pages/blogs/addblog.html',
    categories=categories, blogs=new_blogs)
   


@main.route('/blogs/new/', methods=['GET','POST'])
@login_required
def new_blog():
  categories = Category.query.order_by(Category.id.asc()).all()
  if request.method == 'POST':
    blog = Blog(title=request.form['title'], content=request.form['content'], category_id=request.form['category'], user_id=current_user.id)
    db.session.add(blog)
    db.session.commit()
    flash('blog created successfully', 'success')
    return redirect(url_for('main.index'))
  
  return render_template('pages/blogs/addblog.html', categories=categories)