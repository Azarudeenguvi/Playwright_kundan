from playwright.sync_api import sync_playwright
from sauce_Demo_project.Pages.login import Login


def test_login_case():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        login_=Login(page)
        login_.login()
        page.close()
        browser.close()
