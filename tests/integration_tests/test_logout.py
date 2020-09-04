class TestLogOutShould:

    @staticmethod
    def test_logout_should_redirect_to_login_page(simpyinvoice_client, logged_in_user):
        response = simpyinvoice_client.get('/auth/logout')
        assert response.status_code == 302
        assert response.location.endswith('/auth/login')
