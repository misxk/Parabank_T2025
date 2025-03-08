from faker import Faker


class RegistrationPage():
    def __init__(self, page):
        self.page = page
        self.fake = Faker()
        self.username = None  # Dodajemy zmienne do przechowywania danych
        self.password = None

    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")

    def test_goto(self):
        assert self.page.url == 'https://parabank.parasoft.com/parabank/register.htm', 'Register page is not opened.'

    def register_user(self):
        # generating data
        first_name = self.fake.first_name() # generating first name
        last_name = self.fake.last_name() # generating last name
        address = self.fake.address().split('\n')[0] # generating address
        city = self.fake.city() # generating city
        state = self.fake.state() # generating state
        zip_code = self.fake.zipcode() # generating zip code
        phone_number = self.fake.phone_number() # generating phone number
        ssn = self.fake.ssn() # generating ssn
        self.username = self.fake.user_name()  # storing generated username
        self.password = self.fake.password()  # storing generated password

        # filling the form
        self.page.fill('[name="customer.firstName"]', first_name)# using generated first name
        self.page.fill('[name="customer.lastName"]', last_name) # using generated last name
        self.page.fill('[name="customer.address.street"]', address) # using generated address
        self.page.fill('[name="customer.address.city"]', city) # using generated city
        self.page.fill('[name="customer.address.state"]', state) # using generated state
        self.page.fill('[name="customer.address.zipCode"]', zip_code) # using generated zip code
        self.page.fill('[name="customer.phoneNumber"]', phone_number) # using generated phone number
        self.page.fill('[name="customer.ssn"]', ssn) # using generated ssn
        self.page.fill('[name="customer.username"]', self.username)  # using generated username
        self.page.fill('[name="customer.password"]', self.password)  # using generated passsword
        self.page.fill('[name="repeatedPassword"]', self.password)  # repeat generated password
        self.page.click('input.button[value="Register"]') # clicking register button

    def download_data(self):
        # returning generated data
        return self.username, self.password

    def click_register_button(self):
        self.page.click('input.button[value="Register"]')
