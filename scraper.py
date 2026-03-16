from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Open a new page
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Visit the target page
    url = "https://www.pracuj.pl/"
    page.goto(url)

    # Data extraction logic
    # Data export logic

    # Close the browser 
    browser.close()