from playwright.sync_api import Page
from .base_page import BasePage  # if you have a BasePage; if not, we can change later


class QMSDocumentPage(BasePage):
    """
    Page Object for the (imaginary) QMS Document Initiation screen.

    NOTE: This is a DESIGN based on the SQA Automation Assessment PDFs.
    Locators are placeholders because we don't have a real QMS app.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # === Actions ===

    def goto_document_initiation(self):
        # TODO: real locator when QMS app exists
        # Example:
        # self.page.get_by_role("link", name="QMS").click()
        # self.page.get_by_role("link", name="Document Initiation").click()
        pass

    def fill_document_form(self, sop: str, title: str, approver: str):
        # TODO: replace with real locators later
        # self.page.get_by_label("SOP").fill(sop)
        # self.page.get_by_label("Title").fill(title)
        # self.page.get_by_label("Approver").select_option(label=approver)
        pass

    def submit_document(self):
        # TODO: replace with real button locator
        # self.page.get_by_role("button", name="Submit").click()
        pass

    def verify_document_in_my_records(self, title: str):
        # TODO: replace with real grid / table locators
        # self.page.get_by_role("link", name="My Records").click()
        # self.page.get_by_placeholder("Search").fill(title)
        # assert self.page.get_by_role("cell", name=title).is_visible()
        pass
