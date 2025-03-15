from faker import Faker


class Loan:

    # initializing the class
    def __init__(self, page):
        self.page = page
        self.fake = Faker()

    # entering the Bill Pay page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/requestloan.htm")

    # loan amount
    def loan_amount(self, amount):
        amount = str(self.fake.random_number(5))
        self.page.locator('input[id="amount"]').fill(amount)

    # down payment
    def down_payment(self, payment):
        payment = str(self.fake.random_number(5))
        self.page.locator('input[id="downPayment"]').fill(payment)

    # requesting loan
    def click_apply_now_button(self):
        self.page.click('input.button[value="Apply Now"]')
