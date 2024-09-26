import pytest
import logging

from framework.browser.browser import Browser
from framework.config.driver_list import DriverList

from testfire_tests.config.urls import URLs


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def browser():
    """
    Fixture for WebDriver instance.

    :return: WebDriver instance
    """
    logger.info("Initialize browser.")
    browser = Browser(DriverList.firefox_driver)

    logger.info(f"Navigate to base URL: {URLs.BASE_URL}.")
    browser.navigate_to(URLs.BASE_URL)

    yield browser

    logger.info("Close the browser.")
    browser.close_browser()
