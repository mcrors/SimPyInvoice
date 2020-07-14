import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    SECRET_KEY = os.environ.get("SIMPYINVOICE_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestConfiguration(Configuration):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite:///'


class DevConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')


config_dict = {
    "prod": ProdConfiguration,
    "test": TestConfiguration,
    "dev": DevConfiguration,
    "default": DevConfiguration
}
