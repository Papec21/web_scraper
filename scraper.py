from playwright.sync_api import sync_playwright
import keyboard

with sync_playwright() as p:
    # Open a new page
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Visit the target page
    url = "https://www.pracuj.pl/praca/poznan;wp?rd=0"
    page.goto(url)

    # Data extraction logic
    # Data export logic

    # Close the browser 
    # browser.close()

    # Mockup wait to see if it works
    keyboard.wait('space')