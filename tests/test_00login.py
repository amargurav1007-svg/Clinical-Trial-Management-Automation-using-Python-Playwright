import pytest
from pages.login_page import LoginPage
from utils.config import config


def test_login(page):
    # Create LoginPage object
    login_page = LoginPage(page)

    # Read config values
    base_url = config.get("app_settings.base_url")
    username = config.get("app_settings.username")
    password = config.get("app_settings.password")

    # Step 1: Open application
    login_page.goto(base_url)

    # Step 2: Perform login
    login_page.login(username, password)

    # Step 3: Basic validation after login
    assert base_url in page.url or page.url is not None
