from playwright.sync_api import Page

def test_qms_document_initiation_demoqa(page: Page) -> None:
    page.goto(
        "https://demoqa.com/automation-practice-form",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.fill("#firstName", "Clinical QMS SOP")
    page.fill("#lastName", "SOP-CT-001")
    page.fill("#userEmail", "qa.lead@clinical.com")
