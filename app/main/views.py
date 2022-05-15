from importlib.resources import contents
from flask import render_template,request,redirect,url_for, flash
from ..requests import get_blogs
from . import main
from .. import db, login_manager
from ..models import Blog, User,Comment
from flask_login import  current_user ,login_required
from ..email import mail_message

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def make_blogs(blogs):

  new_blogs = []
  for blog in blogs:
    user = User.query.filter_by(id=blog.user_id).first()
   
    comments = Comment.query.filter_by(blog_id=blog.id).all()
    addblog.append({
      'id': blog.id,
      'title': blog.title,
      'author': blog.author,
      'content': blog.content,
      
      'user': user,
      'upvotes': blog.upvotes,
      'downvotes': blog.downvotes,
      'comments': len(comments)
    })
  return new_blogs

@main.route('/')
def index():
    quotes = get_blogs()
    
    blogs=Blog.query.order_by(Blog.created_at.desc()).all()
    
    return render_template ("pages/index.html",blogs=blogs,quote1=quotes[0],quote2=quotes[2])

@main.route('/blogs/add', methods=['GET','POST'])
@login_required
def addblog():
  if request.method=='POST':
    title=request.form['title']
    author=request.form['author']
    content=request.form['editor1']
    blog=Blog(title=title,author=author,content=content,user_id=current_user.id)

    db.session.add(blog)
    db.session.commit()
    flash('blog created successfully',"success")
    users=User.query.all()
    for user in users:

      mail_message("Welcome to blogs app","email/welcome_user",user.email,user=user)
      print("Email message,..,.,",mail_message)
      return redirect(url_for('main.index'))
  return render_template ('pages/blogs/addblog.html')
   
@main.route('/blogs/view/<int:blog_id>', methods=['GET','POST'])
@login_required
def view_blog(blog_id):
  blog=Blog.query.get(int(blog_id))
  quotes = get_blogs()
    
  blogs=Blog.query.all()
  return render_template('pages/blogs/view.html',blog=blog,quote1=quotes[0],quote2=quotes[2],blogs=blogs,quote3=quotes[3],quote4=quotes[4])


@main.route('/blogs/view/<int:blog_id>', methods=['GET','POST'])
def add_comment(blog_id):
  blog = Blog.query.filter_by(id=blog_id).first()
  if request.method == 'POST':
    content = request.form['comment']
    if blog:
      comment = Comment(blog_id=blog.id, user_id=current_user.id, content=content)
      db.session.add(comment)
      db.session.commit()
      flash('Comment added', 'success')
      return redirect(url_for('main.view_blog', blog_id=blog.id))
    else:
      flash('Pitch not found', 'warning')
      return redirect(url_for('main.index'))
  return redirect(url_for('main.view_blog', blog_id=blog.id))
