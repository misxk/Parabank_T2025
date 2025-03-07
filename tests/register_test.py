from playwright.sync_api import sync_playwright
from classes.homepage import HomePage
from classes.admin_page import AdminPage
from classes.register_page import RegistrationPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    register_page = RegistrationPage(page)
    register_page.goto()
    register_page.register_user()
    admin_page = AdminPage(page)
    admin_page.goto()
    admin_page.click_admin_page()
    admin_page.click_clean_button()
    home_page = HomePage(page)
    home_page.goto()
    if not page.is_closed():
        page.wait_for_url('https://parabank.parasoft.com/parabank/index.htm')
        locator_log_out = page.locator("text= Log Out").is_visible()
        try:
            assert locator_log_out is True
            print(f'log out visible and user is registered successfully')
        except AssertionError:
            print(f'log out not visible')

    browser.close()

