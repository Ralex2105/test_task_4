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
    logging.info("Initialize browser.")
    browser = Browser(DriverList.firefox_driver)

    logging.info(f"Navigate to base URL: {URLs.BASE_URL}.")
    browser.navigate_to(URLs.BASE_URL)

    yield browser

    logging.info("Close the browser.")
    browser.close_browser()
