import pytest
from pages.homepage import HomePage
from pages.driver import PlaywrightBrowser
from pages.register_page import RegistrationPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # creating browser
    browser.launch_browser()  # launching browser
    yield browser  # Returning the browser to tests
    browser.close_browser()  # closing browser

def test_to_check_if_user_can_login(browser):
    # creating objects
    home_page = HomePage(browser.page) # creating homepage object
    admin_page = AdminPage(browser.page) # creating admin page object
    register_page = RegistrationPage(browser.page)  # creating register page object
    page = browser.page # creating page object

    admin_page.goto() # entering admin page
    admin_page.click_clean_button() # cleaning the database

    register_page.goto() # entering register page
    register_page.register_user()  # registration of user

    home_page.log_out() # logging out

    home_page.goto() # entering homepage

    username, password = register_page.download_data()  # downloading created username and password

    page.fill('[name="username"]', username)  # using generated username
    page.fill('[name="password"]', password)  # using generated password

    home_page.log_in() #logging in

    page.wait_for_url('https://parabank.parasoft.com/parabank/overview.htm') # waiting for the page to load
    success_log_in_url = 'https://parabank.parasoft.com/parabank/overview.htm'
    assert success_log_in_url == 'https://parabank.parasoft.com/parabank/overview.htm', 'Login failed'


