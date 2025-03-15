class HomePage:
    # initialize homepage
    def __init__(self, page):
        self.page = page

    # open homepage
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
        self.page.wait_for_selector('input[value="Log In"]', timeout= 10000)
    # log out
    def log_out(self):
        self.page.click('text=Log Out')

    # log in
    def log_in(self):
        self.page.click('text=Log In')
