from utils.config import config
from utils.logger import get_logger

log = get_logger("base")

class BasePage:

    def __init__(self, page):
        self.page = page

    def open_url(self):
        url = config.get_base_url()
        log.info(f"Opening URL: {url}")

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)
