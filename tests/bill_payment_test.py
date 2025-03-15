import pytest
from pages.driver import PlaywrightBrowser
from pages.register_page import RegistrationPage
from pages.bill_payment_page import BillPayPage
from faker import Faker

@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # creating browser
    browser.launch_browser()  # launching browser
    yield browser  # Returning the browser to tests
    browser.close_browser()  # closing browser

def test_to_check_if_user_is_able_to_make_billpay(browser):
    # creating objects
    register_page = RegistrationPage(browser.page)  # creating register page object
    bill_payment_page = BillPayPage(browser.page)

    register_page.goto() # entering register page
    register_page.register_user()  # registration of user

    bill_payment_page.goto()  # entering the Bill Pay page

    fake = Faker()
    account_number = str(fake.random_number(digits=8))  #creating fake account number to have possiblity to return it to the form
    bill_payment_page.page.fill('[name="payee.name"]', fake.name())
    bill_payment_page.page.fill('[name="payee.address.street"]',fake.street_address()) # filling the form with fake address street
    bill_payment_page.page.fill('[name="payee.address.city"]',fake.city()) # filling the form with fake city
    bill_payment_page.page.fill('[name="payee.address.state"]',fake.state()) # filling the form with fake state
    bill_payment_page.page.fill('[name="payee.address.zipCode"]',fake.zipcode()) # filling the form with fake zip code
    bill_payment_page.page.fill('[name="payee.phoneNumber"]', fake.phone_number())
    bill_payment_page.page.fill('[name="payee.accountNumber"]', account_number) # filling the form with fake account number
    bill_payment_page.page.fill('[name="verifyAccount"]', account_number) # repeating same account number
    bill_payment_page.page.fill('[name="amount"]', str(fake.random_number(digits=5))) #converting to string

    bill_payment_page.send_payment_button()  # clicking send payment button

    success_message = browser.page.locator("//*[@id='billpayResult']/h1").text_content()
    assert success_message == 'Bill Payment Complete', 'Bill payment failed'




