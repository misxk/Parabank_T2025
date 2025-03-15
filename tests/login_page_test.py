import pytest
from pages.HomePage import HomePage
from pages.PlaywrightDriver import PlaywrightBrowser
from pages.RegisterPage import RegistrationPage
@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # creating browser
    browser.launch_browser()  # launching browser
    yield browser  # Returning the browser to tests
    browser.close_browser()  # closing browser

def test_to_check_if_user_can_login(browser):
    page = browser.page # creating page object

    register_page = RegistrationPage(browser.page)  # creating register page object
    register_page.goto() # entering register page
    register_page.register_user()  # registration of user

    home_page = HomePage(browser.page)  # creating homepage object
    home_page.log_out() # logging out

    username, password = register_page.get_username_and_password()  # downloading created username and password

    page.fill('[name="username"]', username)  # using generated username
    page.fill('[name="password"]', password)  # using generated password

    home_page.log_in() #logging in

    success_log_in_url = 'https://parabank.parasoft.com/parabank/overview.htm'
    assert success_log_in_url == 'https://parabank.parasoft.com/parabank/overview.htm', 'Login failed'


