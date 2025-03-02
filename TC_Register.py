from playwright.sync_api import sync_playwright
from HomePage import HomePage
from Browser import Driver_Factory
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.goto()
    page.click('text= Register')
    page.wait_for_selector('h1', timeout=5000)
    register_message = 'Signing up is easy!'
    message = page.text_content("h1")
    page.fill('[name="customer.firstName"]', 'student')
    page.fill('[name="customer.lastName"]', 'student')
    page.fill('[name="customer.address.street"]', 'Chopina')
    page.fill('[name="customer.address.city"]', 'Warsaw')
    page.fill('[name="customer.address.state"]', 'Mazowieckie')
    page.fill('[name="customer.address.zipCode"]', '7000')
    page.fill('[name="customer.phoneNumber"]', '+4800000000')
    page.fill('[name="customer.ssn"]', '123456789')
    page.fill('[name="customer.username"]', 'student')
    page.fill('[name="customer.password"]', 'MTEST25')
    page.fill('[name="repeatedPassword"]', 'MTEST25')
    page.click('text= Register')
    page.wait_for_selector('h1', timeout=5000)
    success_message = "Your account was created successfully. You are now logged in."
    message = page.text_content("h1")
    try:
        assert success_message in message
    except AssertionError:
        print(f'Assertion has failed, title is not same as expected {message}')
    browser.close()