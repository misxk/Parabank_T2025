from Page.HomePage import HomePage
from playwright.sync_api import sync_playwright
def test_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        home_page = HomePage(page)
        home_page.goto()
        title = page.title()
        try:
            assert title == "ParaBank | Welcome | Online Banking"
        except AssertionError:
            print (f'Assertion has failed, title is not same as expected {title}')
        browser.close()

test_home_page()