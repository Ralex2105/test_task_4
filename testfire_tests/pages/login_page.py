from selenium.webdriver.common.by import By

from framework.elements.textbox_element import TextBoxElement
from framework.elements.button_element import ButtonElement
from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login page class with basic elements
    """

    __LOGIN_PAGE_USERNAME_FIELD = (By.ID, "uid")
    __LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "passw")
    __LOGIN_PAGE_LOGIN_BUTTON = (By.NAME, "btnSubmit")

    def __init__(self):
        """
        Initializing the login page with basic elements
        """
        self.username_textbox_element = TextBoxElement(self.__LOGIN_PAGE_USERNAME_FIELD)
        self.password_textbox_element = TextBoxElement(self.__LOGIN_PAGE_PASSWORD_FIELD)
        self.login_button_element = ButtonElement(self.__LOGIN_PAGE_LOGIN_BUTTON)

    def enter_username(self, browser, username):
        """
        Enters the username into the username field.

        :param browser: instance Browser
        :param username: Username string
        """
        self.username_textbox_element.enter_text(browser, username)

    def enter_password(self, browser, password):
        """
        Enters the password into the password field.

        :param browser: instance Browser
        :param password: Password string
        """
        self.password_textbox_element.enter_text(browser, password)

    def click_login_button(self, browser):
        """
        Clicks the login button to submit the login form.

        :param browser: instance Browser
        """
        self.login_button_element.click(browser)
