from playwright.sync_api import Page

class AdminPage:
    # Initializing the admin page
    def __init__(self, page: Page):
        self.page = page

    # Entering the admin page
    def goto(self):
        # Entering the admin page
        self.page.goto("https://parabank.parasoft.com/parabank/admin.htm")

    # Cleaning the database
    def click_clean_button(self):
        self.page.click("button:has-text('Clean')") # Click the "Clean" button on the admin page






