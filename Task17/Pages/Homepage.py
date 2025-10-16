class Home:
    def __init__(self,page):
        self.page=page
        self.locator_dashboard=page.locator('p.header-name')
        self.locator_profile=page.locator('div.user-name-div')
        self.locator_logout=page.locator('text=Log out')
        self.locator_close=page.locator('button.custom-close-button')

    def dashboard_is_visible(self):
        return self.locator_dashboard.is_visible()

    def profile_click(self):
        self.locator_profile.click()

    def logout_click(self):
        self.locator_logout.click()

    def close_icon(self):
        self.locator_close.wait_for(state='visible')
        self.locator_close.click()
