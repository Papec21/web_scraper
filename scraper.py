from playwright.sync_api import sync_playwright
import keyboard

with sync_playwright() as p:
    # Open a new page
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Visit the target page
    url = "https://www.pracuj.pl/praca/poznan;wp?rd=0&et=1&sc=0"
    page.goto(url)

    # Click on cookies and terms changes
    try:
        page.locator("[data-test=\"button-submitCookie\"]").click()
        page.get_by_role("button", name="OK, rozumiem").click()
    except:
        pass

    # Wait for data to load
    combined_offers_selector = "[data-test='default-offer'], [data-test='positioned-offer']"
    page.wait_for_selector(combined_offers_selector, timeout=10000)

    # Getting the HTML of the target page
    combined_offers = page.locator(combined_offers_selector).all()
    print(f"Znaleziono {len(combined_offers)} ofert na stronie")

    # Place to store scraped data
    intership_offers = []

    # Data extraction logic

    # Data export logic

    # Close the browser 
    # browser.close()

    # Mockup wait to see if it works
    # keyboard.wait('space')