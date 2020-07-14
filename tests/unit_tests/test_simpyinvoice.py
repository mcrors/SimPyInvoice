from flask import Flask, current_app


class TestSimPyInvoiceShould:

    @staticmethod
    def test_create_flask_app(simpyinvoice_app):
        assert isinstance(simpyinvoice_app, Flask)
        assert current_app.name == 'simpyinvoice'

    @staticmethod
    def test_app_includes_correct_extensions(simpyinvoice_app):
        expected_extensions = ['bootstrap', 'mail', 'sqlalchemy', 'nav_renderers']
        actual_extensions = list(simpyinvoice_app.extensions.keys())
        expected_extensions.sort()
        actual_extensions.sort()
        assert expected_extensions == actual_extensions
