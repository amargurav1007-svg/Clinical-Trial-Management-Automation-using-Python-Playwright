from pages.ae_page import AEPage

def test_ae_reporting_demoqa(page):
    ae = AEPage(page)

    ae.open()

    ae.fill_ae_details(
        pid="AE001",
        etype="Headache",
        desc="Patient reported headache after medication",
        date="10 Jan 2025"
    )

    ae.submit_report()

    assert ae.is_report_submitted() is True
