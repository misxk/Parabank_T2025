from playwright.sync_api import Page

class AdminPage:
    # Initializing the admin page
    def __init__(self, page: Page):
        self.page = page

    # Entering the admin page
    def goto(self):
        # Entering the admin page
        self.page.goto("https://parabank.parasoft.com/parabank/admin.htm")

    # Checking if admin page is opened
    def test_goto(self):
        assert self.page.url == 'https://parabank.parasoft.com/parabank/admin.htm', 'Admin page is not opened.'

    # Cleaning the database
    def click_clean_button(self):
        self.page.click("button:has-text('Clean')") # Click the "Clean" button on the admin page

    # Checking if the database is cleaned
    def verify_database_cleaned(self):
        self.page.wait_for_selector("//*[@id='rightPanel']/p/b", timeout=5000) # Waiting for the page to load
        clean_message = self.page.locator("//*[@id='rightPanel']/p/b").text_content() # Getting the message
        assert "Database Cleaned" in clean_message, 'Database not cleaned.' # Checking if the message is correct




