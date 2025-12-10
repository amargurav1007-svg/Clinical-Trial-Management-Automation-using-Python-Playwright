from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/login")

    def enter_username(self, username: str):
        self.page.locator("#userName").fill(username)

    def enter_password(self, password: str):
        self.page.locator("#password").fill(password)

    def click_login(self):
        self.page.locator("#login").click()

    def get_profile_name(self):
        return self.page.locator("#userName-value").inner_text()
