from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

from flask_login import LoginManager
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

from flask_mail import Mail
mail=Mail()


bootstrap = Bootstrap()
db = SQLAlchemy()



def create_app(config_name):

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Database URL
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

    # Initializing flask extensions
    bootstrap.init_app(app)
    db = SQLAlchemy(app)
    db.create_all()
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app
