import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.guvi.in/")
    page.get_by_role("link", name="Courses", exact=True).nth(1).click()
    page.goto("https://www.guvi.in/courses/?current_tab=paidcourse&language=tamil")
    page.locator("#courses-language-filter-common-top").get_by_text("Tamil").click()
    page.get_by_role("button", name="View More").click()
    page.get_by_role("link", name="Codeigniter in Tamil").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
