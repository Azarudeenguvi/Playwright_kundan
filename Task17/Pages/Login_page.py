class Login:
    def __init__(self,page):
        self.page=page
        self.locator_email=page.get_by_placeholder('Enter your mail')
        self.locator_password=page.get_by_placeholder('Enter your password ')
        self.locator_sign_in=page.get_by_role("button",name='Sign in')
        self.locator_incorrect_pass=page.locator('text=Incorrect password!')

    def email(self,email):
        self.locator_email.fill(email)

    def password(self,password):
        self.locator_password.fill(password)

    def sign_in_btn(self):
        self.locator_sign_in.click()

    def email_is_visible(self):
        return self.locator_email.is_visible()

    def password_is_visible(self):
        return self.locator_password.is_visible()

    def sign_btn_enabled(self):
        return self.locator_sign_in.is_enabled()

    def incorrect_email_visible(self):
        self.locator_incorrect_pass.is_visible()
