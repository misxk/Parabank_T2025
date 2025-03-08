class HomePage:
    # initialize homepage
    def __init__(self, page):
        self.page = page

    # open homepage
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # check if homepage is opened
    def test_goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
        assert self.page.url == "https://parabank.parasoft.com/parabank/index.htm", 'Homepage is not opened.' # asserting if homepage is opened

    # log out and asserting if log in button is visible, since we logged out of an account
    def log_out(self):
        self.page.click('text=Log Out')
        assert self.page.locator('text=Log In').is_visible(), 'Log In button is not visible' # asserting if log in button is visible

    # log in and asserting if log in button is visible, since we logged in to an account
    def log_in(self):
        self.page.click('text=Log In')
        assert self.page.locator ('text=Log Out').is_visible(), 'Log out button is not visible' # asserting if log out button is visible