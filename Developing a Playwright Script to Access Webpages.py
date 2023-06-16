from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Set the user agent to a legitimate one
    page.set_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    # Set the headers for the page
    headers = {
        'Referer': 'https://www.darty.com/nav/extra/vendeur/311731'
    }
    page.set_extra_http_headers(headers)

    # Set the viewport size to a desktop size
    page.set_viewport_size({'width': 1920, 'height': 1080})

    # Navigate to the page
    page.goto('https://www.darty.com/nav/extra/vendeur/311730')

    # Wait for the page to load completely
    page.wait_for_selector('.darty_rating_stars')

    # Get the page content
    content = page.content()

    # Print the page content
    print(content)

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)