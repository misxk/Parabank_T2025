class Transfer:
    # initializing the class
    def __init__(self, page):
        self.page = page

    # entering the Bill Pay page
    def goto(self):
        self.page.goto("https://parabank.parasoft.com/parabank/transfer.htm")

    # transfering funds
    def click_transfer_funds_button(self):
        self.page.click('input.button[value="Transfer"]')