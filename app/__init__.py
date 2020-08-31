import os
from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config_dict

mail = Mail()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(os.environ.get('APP_NAME'))
    app.config.from_object(config_dict[config_name])

    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    from app import models
    return app


def register_blueprints(app):
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

