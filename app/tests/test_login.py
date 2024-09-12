from app.factories.page_factory import PageFactory
from app.config import URLs
from app.config import Credentials
import logging


logging.basicConfig(level=logging.INFO)


def test_login(driver):
    """
    Test the login functionality.

    :param driver: WebDriver instance
    """
    logging.info("Starting the login test")

    login_page = PageFactory.create_login_page(driver)

    logging.info("Navigating to login page")
    driver.get(URLs.LOGIN_URL_BEFORE_AUTH)

    logging.info("Entering username and password")
    login_page.enter_username(Credentials.USERNAME)
    login_page.enter_password(Credentials.PASSWORD)
    login_page.click_login()

    expected_url = URLs.LOGIN_URL_AFTER_AUTH
    actual_url = driver.current_url
    logging.info(f"Expected URL: {expected_url}, Actual URL: {actual_url}")
    assert actual_url == expected_url, f"Login failed. Expected URL: {expected_url}, but got: {actual_url}"

    logging.info("Navigating back to the home page")
    driver.get(URLs.BASE_URL)
    logging.info("Login test completed")