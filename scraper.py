from playwright.sync_api import sync_playwright
import csv
# import keyboard

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

    # Selectors 
    offer_container_selector = "[data-test='default-offer']"
    title_selector = "[data-test='offer-title']"
    company_selector = "[data-test='text-company-name']"

    # Wait for data to load
    page.wait_for_selector(offer_container_selector, timeout=10000)

    # Getting the HTML of the target page
    offer_elements = page.locator(offer_container_selector).all()
    print(f"Znaleziono {len(offer_elements)} ofert na stronie")

    # Place to store scraped data
    offers = []

    # Data extraction logic
    for element in offer_elements:
        try:
            title = element.locator(title_selector).inner_text().strip()
            
            company = ""
            if element.locator(company_selector).count() > 0:
                company = element.locator(company_selector).inner_text().strip()

            offers.append({"id": id, "title": title, "company": company})
            print(f"Pobrano:{id} | {title} | {company}")

        except Exception as e:
            continue

    print(offers)

    # Data export logic
with open("job_offers.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "company"])
    writer.writeheader()
    writer.writerows(offers)
    print("Zapisano")

    # Close the browser 
    # browser.close()

    # Mockup wait to see if it works
    # keyboard.wait('space')