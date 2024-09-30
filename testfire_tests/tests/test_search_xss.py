import logging
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException

from framework.config.test_data import TestData

from testfire_tests.config.urls import URLs
from testfire_tests.pages.landing_page import LandingPage


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_search_xss(browser):
    """
    Test to ensure that the search field is not vulnerable to XSS attacks.

    :param browser: Browser instance
    """

    xss_payload = TestData.XSS_PAYLOAD

    logger.info("Start the XSS test.")
    landing_page = LandingPage()

    logger.info("Navigate to landing page.")
    browser.navigate_to(URLs.BASE_URL)

    logger.info("Enter xss in search field and submit.")
    landing_page.enter_search_query(browser, xss_payload)
    landing_page.submit_search(browser)

    try:
        logger.info("Get page source to check for XSS payload.")
        page_source = browser.get_page_source()
        if xss_payload in page_source:
            logger.info("Potential XSS vulnerability detected: XSS payload found in page source.")
            assert False, "Potential XSS vulnerability detected: XSS payload found in page source."
        else:
            logger.info("No XSS vulnerability detected.")
            assert True, "XSS vulnerability check passed. No XSS payload found."
    except UnexpectedAlertPresentException:
        logger.error("XSS vulnerability detected: Alert appeared")
        assert False, f"XSS vulnerability detected: Alert appeared"

    logger.info("Finish xss search test")
