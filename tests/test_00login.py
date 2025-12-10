import pytest
from pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.enter_username("testuser")
    login.enter_password("Test@123")
    login.click_login()

    profile_name = login.get_profile_name()
    assert profile_name != ""
