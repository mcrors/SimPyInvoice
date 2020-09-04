class TestIndexShould:

    @staticmethod
    def test_index_redirects_to_login_page_if_user_is_not_signed_in(simpyinvoice_client):
        response = simpyinvoice_client.get('/')
        assert response.status_code == 302
        assert '/auth/login' in response.location

    @staticmethod
    def test_index_redirects_to_users_homepage_if_user_is_signed_in(simpyinvoice_client, db_with_one_user, a_test_user):
        simpyinvoice_client.post('/auth/login', data={
            'email': a_test_user['email'],
            'password': a_test_user['password']
        })
        response = simpyinvoice_client.get('/')
        html = response.get_data(as_text=True)
        assert response.status_code == 200
        assert f'Welcome back {a_test_user["first_name"]}' in html
