from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Navigate to the form page
    page.goto("https://demoqa.com/text-box")

    # Fill the form
    page.fill("#userName", "SOP") # doc_type
    page.fill("#userEmail", "QMS Automation Test Document") # title
    page.fill("#currentAddress", "Approver1, QualityManager") # approvers

    # Click the submit button
    page.click("#submit")

    # Wait for a short period to allow the output to render
    page.wait_for_timeout(1000) # Wait for 1 second

    # Get the page content
    html_content = page.content()
    print(html_content)

    browser.close()