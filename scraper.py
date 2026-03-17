from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import keyboard
import httpx

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
    except Exception as e:
        print(f"Błąd przy akceptacji cookies: {e}")

    # Getting the HTML of the target page
    url = "https://www.pracuj.pl/praca/poznan;wp?rd=0&et=1&sc=0"
    response = httpx.get(url)
    html = response.text

    # Wait for website to load
    try:
        page.wait_for_selector(".tiles_o1859gd9 core_n194fgoq", timeout=10000)
    except Exception as e:
        print(f"Błąd: nie znaleziono ofert: {e}")

    
    soup = BeautifulSoup(html, "html.parser")
    # Place to store scraped data
    intership_offers = []

    # Data extraction logic
    offer_elements = soup.select(".tiles_o1859gd9.core_n194fgoq")
    for offer_element in offer_elements:
        # Extraction of job title
        title_element = offer_element.select_one(".text")
        if title_element:
            title = title_element.get_text(strip=True)
            print(title_element)

    # Data export logic

    # Close the browser 
    # browser.close()

    # Mockup wait to see if it works
    keyboard.wait('space')