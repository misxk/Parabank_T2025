import pytest
from faker import Faker
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
    fake = Faker()
    register_page.page.fill('[name="customer.firstName"]', fake.first_name()) # filling the form with fake first name
    register_page.page.fill('[name="customer.lastName"]', fake.last_name()) # filling the form with fake last name
    register_page.page.fill('[name="customer.address.street"]', fake.street_address()) # filling the form with fake address street
    register_page.page.fill('[name="customer.address.city"]', fake.city()) # filling the form with fake city
    register_page.page.fill('[name="customer.address.state"]', fake.state()) # filling the form with fake state
    register_page.page.fill('[name="customer.address.zipCode"]', fake.zipcode()) # filling the form with fake zip code
    register_page.page.fill('[name="customer.phoneNumber"]', fake.phone_number()) # filling the form with fake phone numer
    register_page.page.fill('[name="customer.ssn"]', fake.ssn()) # filling the form with fake customer ssn
    register_page.page.fill('[name="customer.username"]', fake.user_name()) # filling the form with fake username
    password = fake.password() # creating fake password
    register_page.page.fill('[name="customer.password"]', password) # filling the form with fake password
    register_page.page.fill('[name="repeatedPassword"]', password) # repeating the password
    register_page.click_register_button() # clicking register button
# Asserting if register page is opened
    assert browser.page.url == 'https://parabank.parasoft.com/parabank/register.htm', 'Register page is not opened.'
# Waiting for the page to load
    if not browser.page.is_closed():
        browser.page.wait_for_url('https://parabank.parasoft.com/parabank/register.htm')
# Asserting if log out button is visible
    success_message = browser.page.locator("//div[@id='rightPanel']/p").text_content()
    assert success_message == 'Your account was created successfully. You are now logged in.'


