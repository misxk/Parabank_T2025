class HomePage:
    def __init__(self, page):
        self.page = page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    def log_out(self):
        self.page.click('text=Log Out')

    def log_in(self):
        self.page.click('text=Log In')