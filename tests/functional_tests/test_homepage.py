class TestHomepageShould:

    # The User enters the website address and arrives at the home page
    @staticmethod
    def test_succesfully_reach_home_page(simpyinvoice_client):
        response = simpyinvoice_client.get("/")
        assert response.status_code == 200

    # She notices that the title of the website is SimPyInvoice
    @staticmethod
    def test_website_title(simpyinvoice_client):
        response = simpyinvoice_client.get("/")
        html = response.get_data()
        assert b"<title>Home - SimpyInvoice</title>" in html
