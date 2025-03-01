class HomePage:
    def __init__(self, page):
        self.page = page
    def goto(self):
        self.page.goto("https://allegro.pl")
    def get_title(self):
        return self.page.title()