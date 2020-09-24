from tests.functional_tests.func_test_utils import register_via_browser, login_via_browser


def test_user_can_register_and_then_login_then_logout(simpy_test_container, firefox_browser):
    # Edith has heard about a new app to help manage her invoices
    # She opens a browser and navigates to the registration page
    firefox_browser.get('http://127.0.0.1:5000/')

    # She notices that the name of the app is call SimpyInvoice
    assert 'SimpyInvoice' in firefox_browser.title
    # and that she has been redirected to the login page
    assert 'Login' in firefox_browser.title

    # Because she does not yet have an account, she clicks on the register link
    register_link = firefox_browser.find_element_by_id('register')
    register_link.click()

    assert 'Register' in firefox_browser.title

    edith = {
        'first_name': 'Edith',
        'last_name': 'Jones',
        'username': 'edith_jones',
        'email': 'edith@jones.com',
        'password': '123456789'
    }

    register_via_browser(firefox_browser,
                         edith['first_name'],
                         edith['last_name'],
                         edith['username'],
                         edith['email'],
                         edith['password'])

    assert 'Login' in firefox_browser.title

    login_via_browser(firefox_browser, edith['email'], edith['password'])

    welcome_header_elem = firefox_browser.find_element_by_id('welcome')
    assert 'Welcome back Edith' in welcome_header_elem.text

    logout_link = firefox_browser.find_element_by_id('logout')
    logout_link.click()

    assert 'Login' in firefox_browser.title
