from flask import Flask
from simpyinvoice import create_app


class TestSimPyInvoiceShould:

    def test_create_flask_app(self):
        app = create_app('test')
        assert isinstance(app, Flask)
