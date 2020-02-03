from flask import Flask
import pytest
from simpyinvoice import create_app


class TestSimPyInvoiceShould:

    @pytest.mark.unit_test
    @staticmethod
    def test_create_flask_app():
        app = create_app()
        assert isinstance(app, Flask)
