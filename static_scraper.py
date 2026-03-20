from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    url = "https://books.toscrape.com/"
    page.goto(url)

    books = []

    book_elements = page.locator(".product_pod")
    book_elements.first.wait_for()

    for book_element in book_elements.all():
        title_element = book_element.locator("h3 a")
        title = title_element.text_content().strip()

        book = {
            "title": title
        }

        books.append(book)

    print(books)