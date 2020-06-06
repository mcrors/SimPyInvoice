import os
import tempfile
import pytest
from simpyinvoice import create_app


@pytest.fixture()
def client():
    app = create_app('test')
    client = app.test_client()
    app_cntxt = app.app_context()
    app_cntxt.push()
    yield client
    app_cntxt.pop()


class TestHomepageShould:

    def test_redirects_to_login_page(self, client):
        response = client.get("/")
        assert response.status_code == 302
