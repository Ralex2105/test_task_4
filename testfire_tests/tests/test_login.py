import logging
from selenium.webdriver.common.by import By

from testfire_tests.pages.login_page import LoginPage
from testfire_tests.config.urls import URLs
from testfire_tests.config.xpaths import XPaths
from testfire_tests.config.credentials import Credentials

logging.basicConfig(level=logging.DEBUG)



def test_login(browser):
    """
    Test the login functionality.

    :param browser: Browser instance
    """
    logging.info("Start the login test.")

    login_page = LoginPage()

    logging.info(f"Navigate to the login URL. URL: {URLs.LOGIN_URL_BEFORE_AUTH}.")
    browser.navigate_to(URLs.LOGIN_URL_BEFORE_AUTH)

    logging.info(f"Enter username: {Credentials.LOGIN_USERNAME}.")
    login_page.enter_username(browser, Credentials.LOGIN_USERNAME)

    logging.info(f"Enter password.")
    login_page.enter_password(browser, Credentials.LOGIN_PASSWORD)

    logging.info("Click the login button.")
    login_page.click_login_button(browser)

    logging.info("Assert find sign-off button after login.")
    assert browser.find_element(By.XPATH, XPaths.sign_off_button_xpath), "Sign-off button not found."

    logging.info("Finish login test.")
