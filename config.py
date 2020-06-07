import os


class Configuration:
    SECRET_KEY = os.environ.get("SIMPYINVOICE_SECRET_KEY")

class ProdConfiguration(Configuration):
    pass


class TestConfiguration(Configuration):
    TESTING = True
    DEBUG = True


class DevConfiguration(Configuration):
    pass


config_dict = {
    "prod": ProdConfiguration,
    "test": TestConfiguration,
    "dev": DevConfiguration,
    "default": DevConfiguration
}
