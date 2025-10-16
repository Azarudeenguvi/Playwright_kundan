import pytest

from Task17.Pages.Login_page import Login
from Task17.Pages.Homepage import Home

@pytest.mark.usefixtures('page')
class TestZenClass:
    def test_validate_email_password_signin_btn(self,page):
        login=Login(page)
        page.goto("https://www.zenclass.in/login")
        assert login.email_is_visible(),"Email box not visible"
        assert login.password_is_visible(),"password box not visible"
        assert login.sign_btn_enabled(),"sign in button is not enabled "

    def test_login_successful(self,page):
        login=Login(page)
        # page.goto("https://www.zenclass.in/login")
        login.email('azarsece@gmail.com')
        login.password('Azar1509#')
        login.sign_in_btn()
        home=Home(page)
        home.close_icon()
        assert home.dashboard_is_visible(),"Login not successful"

    def test_logout(self,page):
        logout=Home(page)
        logout.profile_click()
        logout.logout_click()

    def test_login_unsuccessful(self,page):
        login=Login(page)
        login.email('test@gmail.com')
        login.password('Azar12345')
        login.sign_in_btn()
        login.incorrect_email_visible()


