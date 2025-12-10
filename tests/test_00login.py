import pytest
from clinical_playwright_project.pages.login_page import LoginPage
from utils.config import config # Import the config object

def test_login(page):
    login_page = LoginPage(page)

    base_url = config.get("app_settings.base_url")
    username = config.get("app_settings.username")
    password = config.get("app_settings.password")

    # Step 1: Open page
    login_page.goto(base_url)

    # Step 2: Login
    login_page.login(username, password)

    # Step 3: Verify login (Add assertions later)
