import logging
from selenium.webdriver.common.by import By

from framework.elements.textbox_element import TextBoxElement
from framework.elements.button_element import ButtonElement
from framework.pages.base_page import BasePage
from framework.cache.cache_element import CacheElement


class LoginPage(BasePage, CacheElement):
    """
    Login page class with basic elements
    """
    __LOGIN_PAGE_USERNAME_TEXTBOX_NAME = "username_textbox_element"
    __LOGIN_PAGE_USERNAME_TEXTBOX = (By.ID, "uid")

    __LOGIN_PAGE_PASSWORD_TEXTBOX_NAME = "password_textbox_element"
    __LOGIN_PAGE_PASSWORD_TEXTBOX = (By.ID, "passw")

    __LOGIN_PAGE_LOGIN_BUTTON_NAME = "login_button_element"
    __LOGIN_PAGE_LOGIN_BUTTON = (By.NAME, "btnSubmit")

    @property
    def username_textbox_element(self):
        """
        Initialize and cache __LOGIN_PAGE_USERNAME_TEXTBOX.

        :return: An instance of TextBoxElement __LOGIN_PAGE_USERNAME_TEXTBOX.
        """
        logging.debug("Get username textbox element.")
        return self.get_cached_element(
            self.__LOGIN_PAGE_USERNAME_TEXTBOX_NAME,
            lambda: TextBoxElement(self.__LOGIN_PAGE_USERNAME_TEXTBOX, self.__LOGIN_PAGE_USERNAME_TEXTBOX_NAME)
        )

    @property
    def password_textbox_element(self):
        """
        Initialize and cache __LOGIN_PAGE_PASSWORD_TEXTBOX.

        :return: An instance of TextBoxElement __LOGIN_PAGE_PASSWORD_TEXTBOX.
        """
        logging.debug("Get password textbox element.")
        return self.get_cached_element(
            self.__LOGIN_PAGE_PASSWORD_TEXTBOX_NAME,
            lambda: TextBoxElement(self.__LOGIN_PAGE_PASSWORD_TEXTBOX, self.__LOGIN_PAGE_PASSWORD_TEXTBOX_NAME)
        )

    @property
    def login_button_element(self):
        """
        Initialize and cache __LOGIN_PAGE_LOGIN_BUTTON.

        :return: An instance of TextBoxElement __LOGIN_PAGE_LOGIN_BUTTON.
        """
        logging.debug("Get login button element.")
        return self.get_cached_element(
            self.__LOGIN_PAGE_LOGIN_BUTTON_NAME,
            lambda: ButtonElement(self.__LOGIN_PAGE_LOGIN_BUTTON, self.__LOGIN_PAGE_LOGIN_BUTTON_NAME)
        )

    def enter_username(self, browser, username):
        """
        Enters the username into the username field.

        :param browser: instance Browser
        :param username: Username string
        """
        logging.debug(f"Enter username: {username} to username textbox")
        self.username_textbox_element.enter_text(browser, username)

    def enter_password(self, browser, password):
        """
        Enters the password into the password field.

        :param browser: instance Browser
        :param password: Password string
        """
        logging.debug("Enter password to password textbox.")
        self.password_textbox_element.enter_text(browser, password)

    def click_login_button(self, browser):
        """
        Clicks the login button to submit the login form.

        :param browser: instance Browser
        """
        logging.debug("Click the login button.")
        self.login_button_element.click(browser)
