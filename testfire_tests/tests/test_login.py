import logging
import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

from testfire_tests.pages.login_page import LoginPage
from testfire_tests.config.urls import URLs
from testfire_tests.config.xpaths import XPaths

logging.basicConfig(level=logging.INFO)
load_dotenv()


def test_login(browser):
    """
    Test the login functionality.

    :param browser: Browser instance
    """
    logging.info("Starting the login test")

    login_page = LoginPage()

    logging.info("Navigating to login page")
    browser.navigate_to(URLs.LOGIN_URL_BEFORE_AUTH)

    logging.info("Entering username and password")
    login_page.enter_username(browser, os.getenv("USERNAME"))
    login_page.enter_password(browser, os.getenv("PASSWORD"))

    logging.info("Click button to submit login and password")
    login_page.click_login_button(browser)

    logging.info("Check unique element in main page after AUTH")
    assert browser.find_element(By.XPATH, XPaths.sign_off_button_xpath)

    logging.info("Finish login test")
