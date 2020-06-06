from flask import Flask
from config import config_dict


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
