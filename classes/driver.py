from playwright.sync_api import sync_playwright

class PlaywrightBrowser:
    # initialize the Playwright browser
    def __init__(self):
        self.browser = None
        self.page = None
        self.p = None

    # launch the Playwright browser
    def launch_browser(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    # close the Playwright browser
    def close_browser(self):
        if self.browser:
            self.browser.close()
        if self.p:
            self.p.stop()

