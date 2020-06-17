from mock import patch
from app.main import views


class TestMainViewsShould:

    def test_index_redirects_and_renders_home(self):
        views.index()
        assert False, "Rework test: Determine what index should do"
