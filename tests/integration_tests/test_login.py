class TestLoginShould:

    @staticmethod
    def test_redirect_to_homepage_after_successfull_login(simpyinvoice_client, db_with_one_user, a_test_user):
        response = simpyinvoice_client.post('/auth/login', data={
            'email': a_test_user['email'], 'password': a_test_user['password']
        })

        assert response.status_code == 302
        assert response.location.endswith('/index')

    @staticmethod
    def test_flash_message_and_show_login_page_after_failed_login(simpyinvoice_client, a_test_user):
        response = simpyinvoice_client.post('/auth/login', data={
            'email': a_test_user['email'], 'password': a_test_user['password']
        })

        assert response.status_code == 200
        assert '<title>  SimpyInvoice  - Login </title>' in response.get_data(as_text=True)
        assert 'Invalid username or password' in response.get_data(as_text=True)
