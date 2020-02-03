from flask import Flask
from simpyinvoice import create_app


class TestSimPyInvoiceShould:

    @staticmethod
    def test_create_flask_app():
        app = create_app()
        assert isinstance(app, Flask)
