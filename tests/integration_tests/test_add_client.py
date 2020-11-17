from flask import template_rendered
import pytest
from app.models import Client


@pytest.fixture()
def client_data():
    return {
            "name": "Super Corp",
            "contact_name": "Batman",
            "contact_email": "batman@supercorp.com"
        }


class TestAddClientShould:

    @staticmethod
    def test_is_directed_to_correct_page(simpyinvoice_client, 
                                         logged_in_user, 
                                         captured_templates):
        response = simpyinvoice_client.get('/client/add')

        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "add_client.html"

    @staticmethod
    def test_redirect_to_homepage_after_succesfully_add_client(simpyinvoice_client, logged_in_user, client_data):
        response = simpyinvoice_client.post('/client/add', data=client_data)

        assert response.status_code == 302
        assert response.location.endswith('/index')

    @staticmethod
    def test_adds_new_client_to_database(simpyinvoice_client, logged_in_user):
        pass
