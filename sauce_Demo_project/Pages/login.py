class Login:
    def __init__(self,page):
        self.page=page
        self.username_locator='id=user-name'
        self.password_locator = 'xpath=//input[@type="password"]'
        self.submit_button_locator = 'id=login-button'

    def login(self):
        self.page.locator(self.username_locator).fill('standard_user')
        self.page.locator(self.password_locator).fill('secret_sauce')
        self.page.locator(self.submit_button_locator).click()





