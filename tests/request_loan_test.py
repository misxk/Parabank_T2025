import pytest
from pages.PlaywrightDriver import PlaywrightBrowser
from pages.register_page import RegistrationPage
from pages.request_loan_page import Loan
from faker import Faker
@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # creating browser
    browser.launch_browser()  # launching browser
    yield browser  # Returning the browser to tests
    browser.close_browser()  # closing browser

def test_to_check_if_user_is_able_request_loan(browser):
    # creating objects
    register_page = RegistrationPage(browser.page)
    page = browser.page
    request_loan_page = Loan(page)

    register_page.goto()  # entering register page
    register_page.register_user()  # registration of user

    request_loan_page.goto() # entering the request loan page

    faker = Faker() # creating faker

    loan_amount = page.locator('[id ="amount"]') # using locator to find the field
    loan_amount.fill(str(faker.random_number(digits=5))) # using random number to fill the field

    down_payment = page.locator('[id="downPayment"]') # using locator to find the field
    down_payment.fill(str(faker.random_number(digits=5))) # using random number to fill the field

    request_loan_page.apply_now() # applying for the loan

    page.wait_for_url('https://parabank.parasoft.com/parabank/requestloan.htm') # waiting for the page to load

    success_message = browser.page.locator("//*[@id='loanRequestApproved']/p[1]").text_content()
    assert success_message == 'Congratulations, your loan has been approved.', 'Loan was rejected'