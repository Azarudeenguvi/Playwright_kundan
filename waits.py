from playwright.sync_api import sync_playwright

def wait_():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True   )
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator('id=user-name').fill('standard_user')
        page.locator('xpath=//input[@type="password"]').fill('secret_sauce')
        page.locator('id=login-button').click()
        print(page.title())
        page.locator('id=add-to-cart-sauce-labs-backpack').click()

        #wait using selector
        page.wait_for_selector('#shopping_cart_container').click()

        #wait using load state
        page.wait_for_load_state()
        page.get_by_role("button",name="Checkout").click()
        page.get_by_placeholder("First Name").fill("mohamed")
        page.get_by_placeholder("Last Name").fill("Azarudeen")
        page.get_by_placeholder("Zip/Postal Code").fill("641008")
        page.locator('#continue').click()
        page.get_by_text("Finish").click()
        successful_order=page.locator('xpath=//h2[@class="complete-header"]').text_content()
        print(successful_order)

        browser.close()

if __name__ == '__main__':
    wait_()