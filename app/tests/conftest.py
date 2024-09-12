import pytest
from app.webdriver.webdriver_singleton import WebDriverSingleton
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="module")
def driver():
    """
    Fixture for WebDriver instance.

    :return: WebDriver instance
    """
    logging.info("Setting up the WebDriver instance")
    driver = WebDriverSingleton.get_driver()
    driver.get("http://testfire.net")
    yield driver
    logging.info("Tearing down the WebDriver instance")
    WebDriverSingleton.quit_driver()
