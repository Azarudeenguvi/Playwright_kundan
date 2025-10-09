from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()