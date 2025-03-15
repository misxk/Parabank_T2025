import pytest
from pages.home_page import HomePage
from pages.PlaywrightDriver import PlaywrightBrowser

@pytest.fixture(scope="function")
def browser():
    browser = PlaywrightBrowser()  # create an instance of PlaywrightBrowser
    browser.launch_browser()  # launch the browser
    yield browser  # yield the browser instance to the test
    browser.close_browser()  # close the browser after the test


def test_home_page(browser):  # use the browser fixture here
    home_page = HomePage(browser.page)  # pass browser.page to HomePage
    home_page.goto()  # navigate to the homepage
    title = browser.page.title()  # get the page title
    assert title == 'ParaBank | Welcome | Online Banking', f'Homepage title is incorrect, expected "ParaBank | Welcome | Online Banking", but got {title}'
