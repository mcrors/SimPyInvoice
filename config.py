import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    SECRET_KEY = os.environ.get("SIMPYINVOICE_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Configuration.init_app(app)


class TestConfiguration(Configuration):
    WTF_CSRF_ENABLED = False
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'test-data.sqlite')

    @classmethod
    def init_app(cls, app):
        Configuration.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class DevConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')


config_dict = {
    "prod": ProdConfiguration,
    "test": TestConfiguration,
    "dev": DevConfiguration,
    "default": DevConfiguration
}
