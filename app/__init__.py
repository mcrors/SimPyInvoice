from flask import Flask
from config import config_dict


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    register_blueprints(app)

    return app

def register_blueprints(app):
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
