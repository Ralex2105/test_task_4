from testfire_tests.config.urls import URLs
from framework.config.test_data import TestData
import logging

from testfire_tests.pages.landing_page import LandingPage

logging.basicConfig(level=logging.INFO)


def test_search_xss(browser):
    """
    Test to ensure that the search field is not vulnerable to XSS attacks.

    :param browser: Browser instance
    """
    logging.info("Starting the XSS test")
    landing_page = LandingPage()

    logging.info("Navigating to landing page")
    browser.navigate_to(URLs.BASE_URL)

    logging.info("Entering xss in search field and submit")
    landing_page.enter_search_query(browser, TestData.XSS_PAYLOAD)
    landing_page.submit_search(browser)

    alert = browser.find_alert()

    if alert[0]:
        logging.info("No XSS vulnerability detected.")
        assert alert[0], "XSS vulnerability check passed. No XSS payload found."
    else:
        logging.error("Potential XSS vulnerability detected: XSS payload found in page source.")
        alert[1].accept()
        assert alert[0], "Potential XSS vulnerability detected: XSS payload found in page source."

    logging.info("Finish xss search test")
