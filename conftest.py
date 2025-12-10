import logging
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def logger():
    logger = logging.getLogger("test-logger")
    logger.setLevel(logging.INFO)
    return logger

@pytest.fixture
def browser(playwright, request):
    headed = request.config.getoption("--headed")
    browser = playwright.chromium.launch(headless=not headed)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
