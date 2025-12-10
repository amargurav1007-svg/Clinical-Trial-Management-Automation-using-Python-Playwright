from pages.base_page import BasePage
from utils.logger import get_logger

log = get_logger("ae")

class AEPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # Form Locators
        self.patient_id = "#firstName"
        self.event_type = "#lastName"
        self.description = "#currentAddress"
        self.date_field = "#dateOfBirthInput"

        # DemoQA required fields
        self.gender = "#gender-radio-1"
        self.mobile = "#userNumber"

        # Submit & Success modal
        self.submit_button = "#submit"
        self.success_modal = "#example-modal-sizes-title-lg"

    def open(self):
        log.info("Opening AE/SAE Page")
        self.open_url()

    def fill_ae_details(self, pid, etype, desc, date):
        log.info("Filling AE details")

        self.fill(self.patient_id, pid)
        self.fill(self.event_type, etype)
        self.fill(self.description, desc)

        self.page.click(self.gender, force=True)
        self.fill(self.mobile, "9999999999")

        self.fill(self.date_field, date)
        log.info("AE details filled")

    def submit_report(self):
        log.info("Submitting AE report")
        self.click(self.submit_button)
        self.page.wait_for_selector(self.success_modal, timeout=5000)

    def is_report_submitted(self):
        log.info("Checking if success modal is visible")
        return self.page.locator(self.success_modal).is_visible()
