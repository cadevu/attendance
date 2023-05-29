import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask import Flask,redirect , url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
index = Blueprint('index','index')


def create_app():
    app = Flask(__name__)
    # config
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)

    # register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .controllers import blueprints
    for bp in blueprints():
        app.register_blueprint(bp, url_prefix = f"/{bp.name}")

    from .auth.loaders import load_prof

    app.register_blueprint(index,url_prefix = '/')

    return app


app = create_app()
