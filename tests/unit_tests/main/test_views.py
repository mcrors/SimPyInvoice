from mock import patch
from app.main import views


class TestMainViewsShould:

    @patch('app.main.views.redirect')
    @patch('app.main.views.url_for')
    def test_index_redirects_and_renders_auth_login(self, mock_url_for, mock_redirect):
        views.index()
        mock_url_for.assert_called_with("auth.login")
        mock_redirect.assert_called_once()
        assert False, "Rework test: Determine what index should do"
