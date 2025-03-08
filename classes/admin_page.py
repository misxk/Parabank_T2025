from playwright.sync_api import Page

class AdminPage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        # Entering the admin page
        self.page.goto("https://parabank.parasoft.com/parabank/admin.htm")

    def test_goto(self):
        assert self.page.url == 'https://parabank.parasoft.com/parabank/admin.htm', 'Admin page is not opened.'
    def click_clean_button(self):
        # Click the "Clean" button on the admin page
        self.page.click("button:has-text('Clean')")

    def verify_database_cleaned(self):
        self.page.wait_for_selector("//*[@id='rightPanel']/p/b", timeout=5000)
        clean_message = self.page.locator("//*[@id='rightPanel']/p/b").text_content()
        assert "Database Cleaned" in clean_message, 'Database not cleaned.'




