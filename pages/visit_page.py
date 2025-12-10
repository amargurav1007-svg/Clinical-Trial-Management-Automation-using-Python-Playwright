from pages.base_page import BasePage

class VisitPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.selenium.dev/selenium/web/web-form.html"
        self.text_box = "input[name='my-text']"
        self.submit_btn = "button"
        self.result = "h1"

    def open(self):
        self.open_url(self.url)

    def fill_visit_details(self, text):
        self.fill(self.text_box, text)

    def submit_form(self):
        self.click(self.submit_btn)

    def verify_visit_created(self):
        return self.is_visible(self.result)
