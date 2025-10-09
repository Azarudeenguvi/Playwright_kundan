from playwright.sync_api import sync_playwright, expect


def assertions_():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        #assertions for username
        expect(page.locator('id=user-name')).to_be_visible()
        # username.fill('standard_user')
        page.locator('id=user-name').fill('standard_user')

        #assertions for password
        expect( page.locator('id=user-name')).to_be_visible()
        # password.fill('secret_sauce')
        page.locator('xpath=//input[@type="password"]').fill('secret_sauce')

        #assertions for submit button

        expect(page.locator('id=login-button')).not_to_be_disabled()
        page.locator('id=login-button').click()
        print(page.title())

        browser.close()

if __name__ == '__main__':
    assertions_()