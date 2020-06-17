class TestHomepageShould:

    # The User enters the website address and arrives at the home page
    @staticmethod
    def test_succesfully_reach_home_page(client):
        response = client.get("/")
        assert response.status_code == 200

    # She notices that the title of the website is SimPyInvoice
    @staticmethod
    def test_website_title(client):
        response = client.get("/")
        html = response.get_date()
        assert "<title>SimPyInvoice</title>" in html

    # She sees that see is invited to log in or to sign up
    @staticmethod
    def test_contains_sign_up_option():
        pass

    @staticmethod
    def test_contains_log_in_form():
        pass

    # She is not a user and so clicks on the sign up link
    @staticmethod
    def test_sign_up_takes_user_to_registration_page():
        pass

    # She is a user and so enters her username and password and is taken to her homepage
    @staticmethod
    def test_log_in_form_submit_takes_user_to_homepage():
        pass

