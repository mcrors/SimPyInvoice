from mock import patch
from simpyinvoice.main import views


class TestMainViewsShould:

    @patch('simpyinvoice.main.views.redirect')
    @patch('simpyinvoice.main.views.url_for')
    def test_index_redirects_and_renders_auth_login(self, mock_url_for, mock_redirect):
        views.index()
        mock_url_for.assert_called_with("auth.login")
        mock_redirect.assert_called_once()

