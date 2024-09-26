import logging
from selenium.webdriver.common.by import By

from testfire_tests.pages.login_page import LoginPage
from testfire_tests.pages.main_page import MainPage
from testfire_tests.config.urls import URLs
from testfire_tests.config.credentials import Credentials


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_login(browser):
    """
    Test the login functionality.

    :param browser: Browser instance
    """
    logger.info("Start the login test.")

    login_page = LoginPage('login page', LoginPage.LOGIN_PAGE_UNIQUE_ELEMENT_LOCATOR)
    main_page = MainPage('main page', MainPage.MAIN_PAGE_UNIQUE_ELEMENT_LOCATOR)

    logger.info(f"Navigate to the login URL. URL: {URLs.LOGIN_URL_BEFORE_AUTH}.")
    browser.navigate_to(URLs.LOGIN_URL_BEFORE_AUTH)

    logger.info(f"Enter username: {Credentials.LOGIN_USERNAME}.")
    login_page.enter_username(browser, Credentials.LOGIN_USERNAME)

    logger.info(f"Enter password.")
    login_page.enter_password(browser, Credentials.LOGIN_PASSWORD)

    logger.info("Click the login button.")
    login_page.click_login_button(browser)

    logger.info("Assert find sign-off button after login.")
    assert main_page.is_open(browser)

    logger.info("Finish login test.")
