from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # ✅ Generic selectors for demo login
        self.username_input = "#userName"
        self.password_input = "#password"
        self.login_button = "#login"

    def goto(self, url: str):
        self.page.goto(url, timeout=60000)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
