import pytest
import logging

from framework.browser.browser import Browser
from framework.config.driver_list import DriverList

from testfire_tests.config.urls import URLs


logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="module")
def browser():
    """
    Fixture for WebDriver instance.

    :return: WebDriver instance
    """
    logging.info("Setting up the WebDriver instance")
    browser = Browser(DriverList.firefox_driver)
    logging.info("Browser instance initialized")
    logging.info("Navigate to" + URLs.BASE_URL)
    browser.navigate_to(URLs.BASE_URL)
    logging.info("Current URL:" + URLs.BASE_URL)
    yield browser
    logging.info("Tearing down the WebDriver instance")
    browser.close_browser()
