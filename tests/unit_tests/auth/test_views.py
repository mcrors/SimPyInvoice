from unittest.mock import Mock, patch
from app.auth.views import register
from app.auth.forms import RegistrationForm


class TestRegisterShould:

    @staticmethod
    @patch('app.auth.views.render_template')
    def test_render_register_page_when_form_not_submitted(render_template_mock, app):
        with app.test_request_context():
            test_form = RegistrationForm()
            with patch('app.auth.views.RegistrationForm', return_value=test_form):
                register()
                render_template_mock.assert_called_once_with('auth/register.html', form=test_form)

    @staticmethod
    @patch('app.auth.views.redirect')
    @patch('app.auth.views.url_for')
    def test_redirect_to_login_page_when_form_is_submitted_and_validated(url_for_mock, redirect_mock, app):
        with app.test_request_context():
            with patch('app.auth.views.User'):
                with patch('app.auth.views.db'):
                    with patch('app.auth.views.RegistrationForm') as form_mock:
                        form_mock.validate_on_submit = Mock(return_value=True)
                        register()
                        url_for_mock.assert_called_once_with('auth.login')
                        redirect_mock.assert_called_once()
