# pages/patient_enrollment_page.py
from pages.base_page import BasePage
from utils.logger import get_logger

log = get_logger("patient")

class PatientEnrollmentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/text-box"

        # Locators
        self.full_name = "#userName"
        self.email = "#userEmail"
        self.current_address = "#currentAddress"
        self.permanent_address = "#permanentAddress"
        self.submit_btn = "#submit"
        self.output_box = "#output"

    def open(self):
        log.info("Opening Patient Enrollment Page")
        self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)

    def fill_form(self, name, email, caddr, paddr):
        self.fill(self.full_name, name)
        self.fill(self.email, email)
        self.fill(self.current_address, caddr)
        self.fill(self.permanent_address, paddr)

    def submit(self):
        self.click(self.submit_btn)

    def is_submitted(self):
        return self.page.locator(self.output_box).is_visible()
