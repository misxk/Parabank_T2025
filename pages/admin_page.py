from playwright.sync_api import Page


class AdminPage:
    # initializing the admin page
    def __init__(self, page: Page):
        self.page = page

    # entering the admin page
    def goto(self):
        # Entering the admin page
        self.page.goto("https://parabank.parasoft.com/parabank/admin.htm")

    # cleaning the database and verifying the success message
    def click_clean_button(self):
        # click the "Clean" button on the admin page
        self.page.click("button:has-text('Clean')")
        # wait for the "Database Cleaned" text to appear (using XPath)
        self.page.wait_for_selector('xpath=//*[@id="rightPanel"]/p/b', timeout=5000)  # Timeout after 5 seconds








