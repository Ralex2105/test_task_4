import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from framework.browser.browser_factory import BrowserFactory
from framework.browser.singleton import SingletonMeta


class Browser(metaclass=SingletonMeta):

    _browser = None

    def __init__(self, browser_type: str = 'chrome', timeout: int = 10):
        """
        Initializes the browser with the specified type using Singleton pattern.

        :param browser_type: Browser type ('chrome', 'firefox')
        :param timeout: Timeout for waits in seconds
        """
        logging.debug(f"Initialize browser with type: {browser_type} and timeout: {timeout} seconds.")
        self._browser = BrowserFactory.initialize_browser(browser_type)
        self.timeout = timeout

    @property
    def browser(self):
        """
        Returns the WebDriver instance.
        """
        logging.debug("Return the Browser instance.")
        return self._browser

    def close_browser(self):
        """
        Closes the browser and quits the WebDriver session.
        """
        logging.debug("Closing the browser.")
        if self._browser:
            self._browser.quit()
            logging.info("Browser closed.")
            BrowserFactory._instance = None
        else:
            logging.warning("No browser instance found to close.")

    def change_browser_type(self, new_browser_type: str):
        """
        Changes the browser type by initializing a new WebDriver instance.

        :param new_browser_type: New browser type ('chrome', 'firefox')
        """
        logging.debug(f"Change browser type from {self._browser.capabilities['browserName']} to {new_browser_type}.")
        if self._browser:
            self._browser.quit()
            BrowserFactory._instance = None
        self._browser = BrowserFactory.initialize_browser(new_browser_type)
        logging.debug(f"Browser type changed to {new_browser_type}.")

    def navigate_to(self, url: str):
        """
        Navigates to the given URL.

        :param url: URL to navigate to
        """
        logging.debug(f"Navigate to URL: {url}")
        self._browser.get(url)

    def get_page_source(self) -> str:
        """
        Returns the page source of the current page.

        :return: Page source as a string
        """
        logging.debug("Get page source.")
        return self._browser.page_source

    def take_screenshot(self, file_path: str):
        """
        Takes a screenshot of the current browser window.

        :param file_path: Path to save the screenshot
        """
        logging.debug(f"Take screenshot and save to {file_path}.")
        self._browser.save_screenshot(file_path)

    def get_title(self) -> str:
        """
        Gets the title of the current page.

        :return: Page title
        """
        logging.debug("Get page title.")
        return self._browser.title

    def get_current_url(self) -> str:
        """
        Gets the current URL of the page.

        :return: Current URL
        """
        logging.debug("Get current URL.")
        return self._browser.current_url

    def wait_for_display_element(self, by: By, value: str):
        """
        Waits for an element to become visible.

        :param by: Locator strategy
        :param value: Locator value
        :return: WebElement
        """
        logging.debug(f"Wait for element for display. Locator: ({by}, {value}).")
        return WebDriverWait(self._browser, self.timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def find_element(self, by: By, value: str):
        """
        Finds an element with a wait for its presence.

        :param by: Locator strategy
        :param value: Locator value
        :return: WebElement
        """
        logging.debug(f"Find element. Locator: ({by}, {value}).")
        return WebDriverWait(self._browser, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_alert(self):
        """
        Waits for an alert to be present.

        :return: Alert instance
        """
        logging.debug("Wait for alert.")
        return WebDriverWait(self._browser, self.timeout).until(
            EC.alert_is_present()
        )
