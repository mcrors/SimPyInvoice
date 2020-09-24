def test_user_can_register_and_then_login_then_logout(simpy_test_container,
                                                      firefox_browser,
                                                      register_and_login):

    # Arther has signed up to a new online invoicing app
    # He would now like to create some clients so that he can start tracking invoices against them
    firefox_browser.get('http://127.0.0.1:5000/')
    welcome_header_elem = firefox_browser.find_element_by_id('welcome')
    assert 'Welcome back Arthur' in welcome_header_elem.text

    # He finds the link to add a new client and clicks on it
    new_client_link = firefox_browser.find_element_by_id('add-new-client')
    new_client_link.click()

    # He notices that he has landed on the add new client page
    # as he can see that the title of the page is New Client
    assert 'New Client' in firefox_browser.title

    # He is presented with a form to enter the details of the new client.
    # This includes the clients name, a client contact name, an an email for that contact
    client_name_input_elem = firefox_browser.find_element_by_id('client_name')
    client_name_input_elem.send_keys('The Very Big Corporation Of America')
    last_name_input_elem = firefox_browser.find_element_by_id('contact_name')
    last_name_input_elem.send_keys('Harry')
    email_input_elem = firefox_browser.find_element_by_id('contact_email')
    email_input_elem.send_keys('harry@corp.com')

    submit_elem = firefox_browser.find_element_by_id('submit')
    submit_elem.click()

    # After clicking on the Create new client button, he finds that he has been redirected back to his
    # homepage. Here he can now see that the new client has been added to a list of clients.
    assert False
