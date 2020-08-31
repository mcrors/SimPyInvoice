from selenium import webdriver


def test_user_can_register_and_then_login(flask_test_server):
    # Edith has heard about a new app to help manage her invoices
    # She opens a browser and navigates to the registration page
    browser = webdriver.Firefox()
    browser.get('http://127.0.0.1:5000/')

    # She notices that the name of the app is call SimpyInvoice
    assert 'SimpyInvoice' in browser.title
    # and that she has been redirected to the login page
    assert 'Login' in browser.title

    # Because she does not yet have an account, she clicks on the register link
    register_link = browser.find_element_by_id('register')
    register_link.click()

    assert 'Register' in browser.title

    # She enters in her details into the registration form
    first_name_input_elem = browser.find_element_by_id('first_name')
    first_name_input_elem.send_keys('Edith')
    last_name_input_elem = browser.find_element_by_id('last_name')
    last_name_input_elem.send_keys('Jones')
    username_input_elem = browser.find_element_by_id('username')
    username_input_elem.send_keys('edith_jones')
    email_input_elem = browser.find_element_by_id('email')
    email_input_elem.send_keys('edith@jones.com')
    password_input_elem = browser.find_element_by_id('password')
    password_input_elem.send_keys('123456789')
    confirm_password_input_elem = browser.find_element_by_id('password_2')
    confirm_password_input_elem.send_keys('123456789')

    # She hits the register button and is redirected to the login page
    register_elem = browser.find_element_by_id('submit')
    register_elem.click()

    assert 'Login' in browser.title

    browser.quit()
