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
