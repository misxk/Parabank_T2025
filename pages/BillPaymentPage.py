from playwright.sync_api import Page
from faker import Faker
class BillPayPage:
    # initializing the class
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker
        self.payee_account = None

    # entering the Bill Pay page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/billpay.htm")

    # generating data for payee
    def payee_information(self):
        payee_name = self.fake.first_name() + ' ' + self.fake.last_name() # generating payee name
        payee_address = self.fake.address().split('\n')[0] # generating payee address
        payee_city = self.fake.city() # generating payee city
        payee_state = self.fake.state() # generating payee state
        payee_zip_code = self.fake.zipcode() # generating payee zip code
        payee_phone_number = self.fake.phone_number() # generating payee phone number
        payee_account = self.fake.account_numer() # generating payee account
        self.payee_account = payee_account # storing payee account
        amount = self.fake.amount() # generating amount

        # filling the information required to pay
        self.page.fill('[name="payee.name"]', payee_name) # using generated payee name
        self.page.fill('[name="payee.address.street"]', payee_address) # using generated payee address
        self.page.fill('[name="payee.address.city"]', payee_city) # using generated payee city
        self.page.fill('[name="payee.address.state"]', payee_state) # using generated payee state
        self.page.fill('[name="payee.address.zipCode"]', payee_zip_code) # using generated payee zip code
        self.page.fill('[name="payee.phoneNumber"]', payee_phone_number) # using generated payee phone number
        self.page.fill('[name="payee.accountNumber"]', self.payee_account) # using generated payee account
        self.page.fill('[name="verifyAccount"]', self.payee_account) # verifying the account
        self.page.fill('[name="amount"]', amount) # using generated amount
        self.page.click('input.button[value="Register"]') # clicking register

    # sending the payment
    def send_payment_button(self):
        self.page.click('input.button[value="Send Payment"]')