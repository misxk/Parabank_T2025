import pytest
from pages.homepage import HomePage
from pages.driver import PlaywrightBrowser

@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # Create an instance of PlaywrightBrowser
    browser.launch_browser()  # Launch the browser
    yield browser  # Yield the browser instance to the test
    browser.close_browser()  # Close the browser after the test


def test_home_page(browser):  # Use the browser fixture here
    home_page = HomePage(browser.page)  # pass browser.page to HomePage
    home_page.goto()  # navigate to the homepage
    title = browser.page.title()  # get the page title
    assert title == 'ParaBank | Welcome | Online Banking', f'Homepage title is incorrect, expected "ParaBank | Welcome | Online Banking", but got {title}'
