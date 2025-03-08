from faker import Faker


class RegistrationPage():
    def __init__(self, page):
        self.page = page
        self.fake = Faker()
        self.username = None  # Dodajemy zmienne do przechowywania danych
        self.password = None

    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")

    def register_user(self):
        # generating data
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        address = self.fake.address().split('\n')[0]
        city = self.fake.city()
        state = self.fake.state()
        zip_code = self.fake.zipcode()
        phone_number = self.fake.phone_number()
        ssn = self.fake.ssn()
        self.username = self.fake.user_name()  # Przechowywanie wygenerowanego username
        self.password = self.fake.password()  # Przechowywanie wygenerowanego password

        # filling the form
        self.page.fill('[name="customer.firstName"]', first_name)
        self.page.fill('[name="customer.lastName"]', last_name)
        self.page.fill('[name="customer.address.street"]', address)
        self.page.fill('[name="customer.address.city"]', city)
        self.page.fill('[name="customer.address.state"]', state)
        self.page.fill('[name="customer.address.zipCode"]', zip_code)
        self.page.fill('[name="customer.phoneNumber"]', phone_number)
        self.page.fill('[name="customer.ssn"]', ssn)
        self.page.fill('[name="customer.username"]', self.username)  # Wykorzystanie wygenerowanego username
        self.page.fill('[name="customer.password"]', self.password)  # Wykorzystanie wygenerowanego password
        self.page.fill('[name="repeatedPassword"]', self.password)  # Wykorzystanie wygenerowanego password
        self.page.click('input.button[value="Register"]')

    def download_data(self):
        # returning generated data
        return self.username, self.password

    def click_register_button(self):
        self.page.click('input.button[value="Register"]')
