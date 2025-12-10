from playwright.sync_api import Page
from .base_page import BasePage


class QMSAuditPage(BasePage):
    """
    Design-only Page Object for Protocol Audit (QMS Module)

    This represents:
    - Clinical Protocol Audits
    - Site Audits
    - Sponsor Audits
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # =========================
    # PROTOCOL AUDIT - DESIGN
    # =========================

    def goto_protocol_audit(self):
        """Navigate to QMS > Audit Management > Protocol Audit"""
        # TODO: Replace with real locators when QMS app is available
        # self.page.get_by_role("link", name="QMS").click()
        # self.page.get_by_role("link", name="Audit Management").click()
        # self.page.get_by_role("link", name="Protocol Audit").click()
        pass

    def create_protocol_audit(self, protocol_id: str, site_name: str, auditor: str):
        """
        Create a new Protocol Audit
        """
        # TODO: real locators later
        # self.page.get_by_label("Protocol ID").fill(protocol_id)
        # self.page.get_by_label("Site Name").fill(site_name)
        # self.page.get_by_label("Auditor").fill(auditor)
        # self.page.get_by_role("button", name="Create Audit").click()
        pass

    def add_audit_finding(self, finding_type: str, description: str):
        """
        Add audit finding (Major / Minor)
        """
        # TODO: real locators later
        # self.page.get_by_label("Finding Type").select_option(label=finding_type)
        # self.page.get_by_label("Description").fill(description)
        # self.page.get_by_role("button", name="Add Finding").click()
        pass

    def submit_audit(self):
        """
        Submit audit for CAPA triggering
        """
        # TODO: real locators later
        # self.page.get_by_role("button", name="Submit Audit").click()
        pass