import pytest
from app.models import User


@pytest.fixture()
def registration_data():
    return {
        'first_name': 'Johnny',
        'last_name': 'Malone',
        'username': 'jm',
        'email': 'jm@malone.com',
        'password': 'my_cats_name',
        'password_2': 'my_cats_name'
    }


class TestRegisterShould:

    @staticmethod
    def test_successful_registration_redirects_to_login_page(simpyinvoice_client, registration_data):
        response = simpyinvoice_client.post('/auth/register', data=registration_data)
        assert response.status_code == 302
        assert response.location.endswith('/auth/login')

    @staticmethod
    def test_adds_a_new_user_to_the_database(simpyinvoice_client, registration_data):
        simpyinvoice_client.post('/auth/register', data=registration_data)
        user = User.query.filter_by(email=registration_data['email']).first()
        assert user is not None
