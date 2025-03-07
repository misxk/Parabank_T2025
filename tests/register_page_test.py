import pytest
from classes.admin_page import AdminPage
from classes.register_page import RegistrationPage
from classes.homepage import HomePage
from classes.driver import PlaywrightBrowser

# Fixture to launch and close browser
@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()
    browser.launch_browser()
    yield browser  # Returning the browser to tests
    browser.close_browser()  # After tests closing the browser

def test_to_check_if_user_can_register(browser):
    admin_page = AdminPage(browser.page)
    admin_page.goto()
    admin_page.click_admin_page()
    admin_page.click_clean_button()
    home_page = HomePage(browser.page)
    home_page.goto()
    # Asserting if homepage is opened
    assert browser.page.url == 'https://parabank.parasoft.com/parabank/index.htm', 'Homepage is not opened.'
    register_page = RegistrationPage(browser.page)
    register_page.goto()
    register_page.page.fill('[name="customer.firstName"]', 'student')
    register_page.page.fill('[name="customer.lastName"]', 'student')
    register_page.page.fill('[name="customer.address.street"]', 'Chopina')
    register_page.page.fill('[name="customer.address.city"]', 'Warsaw')
    register_page.page.fill('[name="customer.address.state"]', 'Mazowieckie')
    register_page.page.fill('[name="customer.address.zipCode"]', '7000')
    register_page.page.fill('[name="customer.phoneNumber"]', '+4800000000')
    register_page.page.fill('[name="customer.ssn"]', '123456789')
    register_page.page.fill('[name="customer.username"]', 'MTEST25')
    register_page.page.fill('[name="customer.password"]', 'MTEST25')
    register_page.page.fill('[name="repeatedPassword"]', 'MTEST25')
    register_page.click_register_button()
# Asserting if register page is opened
    assert browser.page.url == 'https://parabank.parasoft.com/parabank/register.htm', 'Register page is not opened.'
# Waiting for the page to load
    if not browser.page.is_closed():
        browser.page.wait_for_url('https://parabank.parasoft.com/parabank/register.htm')
# Asserting if log out button is visible
    success_message = browser.page.locator("//div[@id='rightPanel']/p").text_content()
    assert success_message == 'Your account was created successfully. You are now logged in.'


