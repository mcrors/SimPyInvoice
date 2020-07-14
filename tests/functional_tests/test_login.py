class TestLoginShould:

    # The User arrives at the Login page
    @staticmethod
    def test_succesfully_reach_login_page(client):
        response = client.get('/auth/login')
        assert response.status_code == 200
#
#     # She sees that see is invited to log in or to sign up
#     @staticmethod
#     def test_contains_sign_up_option():
#         assert False, "Complete the test"
#
#     @staticmethod
#     def test_contains_log_in_form():
#         assert False, "Complete the test"
#
#     # She is not a user and so clicks on the sign up link
#     @staticmethod
#     def test_sign_up_takes_user_to_registration_page():
#         assert False, "Complete the test"
#
#     # She is a user and so enters her username and password and is taken to her homepage
#     @staticmethod
#     def test_log_in_form_submit_takes_user_to_homepage():
#         assert False, "Complete the test"
