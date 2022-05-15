from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=5,max=20)])
    fullname = StringField('fullname',validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Password',validators =[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
