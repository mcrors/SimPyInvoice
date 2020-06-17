import os
from flask import Flask
from config import config_dict


def create_app(config_name):
    app = Flask(os.environ.get('APP_NAME'))
    app.config.from_object(config_dict[config_name])

    register_blueprints(app)

    return app


def register_blueprints(app):
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
