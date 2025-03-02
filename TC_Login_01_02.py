from playwright.sync_api import sync_playwright
from Page.HomePage import HomePage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.goto()
    page.fill('[name="username"]', 'xyzxx')
    page.fill('[name="password"]', 'MTEST25')
    page.click('text=Log In')
    page.wait_for_selector('h1', timeout= 5000)
    success_message = "Accounts Overview"
    message = page.text_content("h1")
    try:
        assert success_message in message
    except AssertionError:
        print (f'Assertion has failed, title is not same as expected {message}')
    browser.close()
