class HomePage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
    def test_goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
        assert self.page.url == "https://parabank.parasoft.com/parabank/index.htm", 'Homepage is not opened.'

    def log_out(self):
        self.page.click('text=Log Out')
        assert self.page.locator('text=Log In').is_visible(), 'Log In button is not visible'

    def log_in(self):
        self.page.click('text=Log In')
        assert self.page.locator ('text=Log Out').is_visible(), 'Log out button is not visible'