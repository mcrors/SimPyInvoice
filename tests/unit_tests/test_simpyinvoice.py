from flask import Flask, current_app


class TestSimPyInvoiceShould:

    @staticmethod
    def test_create_flask_app(app):
        assert isinstance(app, Flask)
        assert current_app.name == 'simpyinvoice'

    @staticmethod
    def test_app_includes_correct_extensions(app):
        expected_extensions = ['bootstrap', 'mail', 'sqlalchemy', 'nav_renderers', 'migrate', 'wtf']
        actual_extensions = list(app.extensions.keys())
        expected_extensions.sort()
        actual_extensions.sort()
        assert expected_extensions == actual_extensions
