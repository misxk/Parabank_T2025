import pytest
from pages.homepage import HomePage
from pages.driver import PlaywrightBrowser
from pages.register_page import RegistrationPage
from pages.admin_page import AdminPage
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
    home_page = HomePage(browser.page)
    admin_page = AdminPage(browser.page)
    register_page = RegistrationPage(browser.page)
    page = browser.page
    request_loan_page = Loan(page)

    admin_page.goto() # entering the admin page
    admin_page.click_clean_button()  # cleaning the database

    register_page.goto()  # entering register page
    register_page.register_user()  # registration of user

    home_page.log_out() # logging out
    home_page.goto() # entering homepage

    username, password = register_page.download_data()  # downloading created username and password

    page.fill('[name="username"]', username)  # using generated username
    page.fill('[name="password"]', password)  # using generated password

    home_page.log_in() #logging in

    page.wait_for_url('https://parabank.parasoft.com/parabank/overview.htm') # waiting for the page to load

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