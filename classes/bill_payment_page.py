from playwright.sync_api import Page
from faker import Faker
class BillPayPage:

    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker
        self.payee_account = None

    def goto(self):
        # entering the Bill Pay page
        self.page.goto("https://parabank.parasoft.com/parabank/billpay.htm")

    def test_goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/billpay.htm")
        assert self.page.url == "https://parabank.parasoft.com/parabank/billpay.htm"
    def payee_information(self):
        # generating data for payee
        payee_name = self.fake.first_name() + ' ' + self.fake.last_name()
        payee_address = self.fake.address().split('\n')[0]
        payee_city = self.fake.city()
        payee_state = self.fake.state()
        payee_zip_code = self.fake.zipcode()
        payee_phone_number = self.fake.phone_number()
        payee_account = self.fake.account_numer()
        self.payee_account = payee_account
        amount = self.fake.amount()

        # filling the information required to pay
        self.page.fill('[name="payee.name"]', payee_name)
        self.page.fill('[name="payee.address.street"]', payee_address)
        self.page.fill('[name="payee.address.city"]', payee_city)
        self.page.fill('[name="payee.address.state"]', payee_state)
        self.page.fill('[name="payee.address.zipCode"]', payee_zip_code)
        self.page.fill('[name="payee.phoneNumber"]', payee_phone_number)
        self.page.fill('[name="payee.accountNumber"]', self.payee_account)
        self.page.fill('[name="verifyAccount"]', self.payee_account)
        self.page.fill('[name="amount"]', amount)
        self.page.click('input.button[value="Register"]')

    def send_payment_button(self):
        self.page.click('input.button[value="Send Payment"]')