class Transfer:
    # initializing the class
    def __init__(self, page):
        self.page = page

    # entering the Bill Pay page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/transfer.htm")

    # transfering funds
    def transfer_funds(self):
        self.page.click('input.button[value="Transfer"]')