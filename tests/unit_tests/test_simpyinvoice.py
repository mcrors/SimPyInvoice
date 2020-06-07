import os
from flask import Flask, current_app
from app import create_app


class TestSimPyInvoiceShould:

    @staticmethod
    def test_create_flask_app(simpyinvoice_app):
        assert isinstance(simpyinvoice_app, Flask)
        assert current_app.name == 'simpyinvoice'
