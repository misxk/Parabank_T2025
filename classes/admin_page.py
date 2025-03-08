from playwright.sync_api import Page

class AdminPage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        # entering the homepage
        self.page.goto("https://parabank.parasoft.com/parabank/admin.htm")

    def click_clean_button(self):
        # Click button "clean" in admin page
        self.page.click("button:has-text('Clean')")