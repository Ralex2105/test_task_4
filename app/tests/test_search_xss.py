from app.factories.page_factory import PageFactory
from selenium.common.exceptions import TimeoutException
from app.config import URLs
from app.config import TestData
import logging

logging.basicConfig(level=logging.INFO)


def test_search_xss(driver):
    """
    Test to ensure that the search field is not vulnerable to XSS attacks.

    :param driver: WebDriver instance
    """
    logging.info("Starting the XSS test")

    search_page = PageFactory.create_search_page(driver)

    xss_payload = TestData.XSS_PAYLOAD
    logging.info("Entering XSS payload into search field")
    search_page.enter_search_query(xss_payload)
    search_page.submit_search()

    try:
        alert = search_page.wait_for_alert()
        alert_text = alert.text
        alert.accept()

        logging.error("XSS vulnerability detected: Alert with text '%s' appeared", alert_text)
        assert False, f"XSS vulnerability detected: Alert with text '{alert_text}' appeared"

    except TimeoutException:
        page_source = driver.page_source

        if xss_payload in page_source:
            logging.error("Potential XSS vulnerability detected: XSS payload found in page source.")
            assert False, "Potential XSS vulnerability detected: XSS payload found in page source."
        else:
            logging.info("No XSS vulnerability detected.")
            assert True, "XSS vulnerability check passed. No XSS payload found."

    logging.info("Navigating back to the home page")
    driver.get(URLs.BASE_URL)