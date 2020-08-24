from unittest.mock import Mock, patch
from wtforms import ValidationError
import pytest
from app.auth.forms import RegistrationForm
from app.models import User
from app import db


class TestRegistrationFormShould:

    @staticmethod
    def test_raise_error_when_existing_email_is_used_again(db_with_one_user, simpyinvoice_app):
        with simpyinvoice_app.test_request_context():
            r = RegistrationForm()
            field = Mock()
            field.data = 'sir.lancelot@camolot.com'
            with pytest.raises(ValidationError):
                r.validate_email(field)

    @staticmethod
    def test_not_raise_error_when_new_email_is_used(db_with_one_user, simpyinvoice_app):
        with simpyinvoice_app.test_request_context():
            r = RegistrationForm()
            field = Mock()
            field.data = 'sir.arthur@camolot.com'
            r.validate_email(field)
            assert True

    @staticmethod
    def test_raise_error_when_existing_username_is_used_again(db_with_one_user, simpyinvoice_app):
        with simpyinvoice_app.test_request_context():
            r = RegistrationForm()
            field = Mock()
            field.data = 'sir_lancelot'
            with pytest.raises(ValidationError):
                r.validate_username(field)

    @staticmethod
    def test_not_raise_error_when_new_username_is_used(db_with_one_user, simpyinvoice_app):
        with simpyinvoice_app.test_request_context():
            r = RegistrationForm()
            field = Mock()
            field.data = 'sir_arthur'
            r.validate_username(field)
            assert True
