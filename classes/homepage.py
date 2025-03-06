class HomePage:
    def __init__(self, page):
        self.page = page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
