from app.pages.base_page import BasePage
from app.config import Locators


class LoginPage(BasePage):

    def enter_username(self, username: str):
        """
        Enters the username into the username field.

        :param username: Username string
        """
        self.enter_text(*Locators.LOGIN_PAGE_USERNAME_FIELD, username)

    def enter_password(self, password: str):
        """
        Enters the password into the password field.

        :param password: Password string
        """
        self.enter_text(*Locators.LOGIN_PAGE_PASSWORD_FIELD, password)

    def click_login(self):
        """
        Clicks the login button to submit the login form.
        """
        self.click_element(*Locators.LOGIN_PAGE_LOGIN_BUTTON)
