import pytest
from pages.PlaywrightDriver import PlaywrightBrowser
from pages.register_page import RegistrationPage
from pages.transfer_funds_page import Transfer
from faker import Faker

@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # creating browser
    browser.launch_browser()  # launching browser
    yield browser  # Returning the browser to tests
    browser.close_browser()  # closing browser

def test_to_check_if_user_is_able_to_make_transfer_funds_operation(browser):
    # creating objects
    register_page = RegistrationPage(browser.page)  # creating register page object
    page = browser.page # creating page object

    register_page.goto() # entering register page
    register_page.register_user()  # registration of user

    page.wait_for_url('https://parabank.parasoft.com/parabank/register.htm') # waiting for the page to load

    transfer_funds_page = Transfer(browser.page) # creating transfer funds page object

    transfer_funds_page.goto()  # entering the transfer funds page

    page.wait_for_url('https://parabank.parasoft.com/parabank/transfer.htm')

    faker = Faker()

    amount_to_transfer = page.locator('[id ="amount"]')

    amount_to_transfer.fill(str(faker.random_number(digits=5))) # filling the fake 5 digit amount

    transfer_funds_page.transfer_funds() # transfering funds

    page.wait_for_url('https://parabank.parasoft.com/parabank/transfer.htm') # waiting for the page to load

    success_message = browser.page.locator("//*[@id='showResult']/h1").text_content() # getting the success message
    assert success_message == 'Transfer Complete!', 'Transfer has failed.' # checking the success message




