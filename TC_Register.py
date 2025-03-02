from playwright.sync_api import sync_playwright
from Page.HomePage import HomePage
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.goto()
    if not page.is_closed():
        page.click('text= Register')
        page.fill('[name="customer.firstName"]', 'student')
        page.fill('[name="customer.lastName"]', 'student')
        page.fill('[name="customer.address.street"]', 'Chopina')
        page.fill('[name="customer.address.city"]', 'Warsaw')
        page.fill('[name="customer.address.state"]', 'Mazowieckie')
        page.fill('[name="customer.address.zipCode"]', '7000')
        page.fill('[name="customer.phoneNumber"]', '+4800000000')
        page.fill('[name="customer.ssn"]', '123456789')
        page.fill('[name="customer.username"]', 'xyz')
        page.fill('[name="customer.password"]', 'MTEST25')
        page.fill('[name="repeatedPassword"]', 'MTEST25')
        page.click('input.button[value="Register"]')
        page.wait_for_url('https://parabank.parasoft.com/parabank/register.htm')
        locator_log_out = page.locator("text= Log Out").is_visible()
        try:
            assert locator_log_out is True
        except AssertionError:
            print(f'log out not visible')
            try:
                assert page.url.endswith("/register.htm"), "Assertion failed: URL is incorrect after registration"
            except AssertionError:
                print(f'log out not visible')


    browser.close()