class RegistrationPage():
    def __init__(self, page):
        self.page = page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")
    def register_user(self):
        self.page.fill('[name="customer.firstName"]', 'student')
        self.page.fill('[name="customer.lastName"]', 'student')
        self.page.fill('[name="customer.address.street"]', 'Chopina')
        self.page.fill('[name="customer.address.city"]', 'Warsaw')
        self.page.fill('[name="customer.address.state"]', 'Mazowieckie')
        self.page.fill('[name="customer.address.zipCode"]', '7000')
        self.page.fill('[name="customer.phoneNumber"]', '+4800000000')
        self.page.fill('[name="customer.ssn"]', '123456789')
        self.page.fill('[name="customer.username"]', 'MTEST25')
        self.page.fill('[name="customer.password"]', 'MTEST25')
        self.page.fill('[name="repeatedPassword"]', 'MTEST25')
        self.page.click('input.button[value="Register"]')
        self.page.wait_for_url('https://parabank.parasoft.com/parabank/register.htm')