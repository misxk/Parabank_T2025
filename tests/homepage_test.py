'''Test if title of Parabank is correct'''
from classes.homepage import HomePage
from playwright.sync_api import sync_playwright
def test_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        home_page = HomePage(page)
        home_page.goto()
        title = page.title()
        try:
            assert title == "ParaBank | Welcome | Online Banking"
        except AssertionError:
            print (f'Assertion has failed, title is not same as expected')
        browser.close()

test_home_page()