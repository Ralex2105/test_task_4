from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from framework.browser.browser_factory import BrowserFactory


class Browser:

    def __init__(self, browser_type: str = 'chrome', timeout: int = 10):
        """
        Initializes the browser with the specified type using Singleton pattern.

        :param browser_type: Browser type ('chrome', 'firefox')
        :param timeout: Timeout for waits in seconds
        """
        self.browser_factory = BrowserFactory(browser_type)
        self.driver = self.browser_factory.driver
        self.timeout = timeout

    def navigate_to(self, url: str):
        """
        Navigates to the given URL.

        :param url: URL to navigate to
        """
        self.driver.get(url)

    def get_page_source(self) -> str:
        """
        Returns the page source of the current page.

        :return: Page source as a string
        """
        return self.driver.page_source

    def close_browser(self):
        """
        Closes the browser using the Singleton instance.
        """
        self.browser_factory.close_browser()

    def take_screenshot(self, file_path: str):
        """
        Takes a screenshot of the current browser window.

        :param file_path: Path to save the screenshot
        """
        self.driver.save_screenshot(file_path)

    def get_title(self) -> str:
        """
        Gets the title of the current page.

        :return: Page title
        """
        return self.driver.title

    def get_current_url(self) -> str:
        """
        Gets the current URL of the page.

        :return: Current URL
        """
        return self.driver.current_url

    def wait_for_display_element(self, by: By, value: str):
        """
        Waits for an element to become visible.

        :param by: Locator strategy
        :param value: Locator value
        :return: WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def find_element(self, by: By, value: str):
        """
        Finds an element with a wait for its presence.

        :param by: Locator strategy
        :param value: Locator value
        :return: WebElement
        """

        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def change_browser_type(self, new_browser_type: str):
        """
        Changes the browser type using the Singleton instance.

        :param new_browser_type: New browser type ('chrome', 'firefox')
        """
        self.browser_factory.change_browser_type(new_browser_type)
        self.driver = self.browser_factory.driver

    def find_alert(self):
        """
        Check alert in Browser
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        except TimeoutException:
            return True
        else:
            return False
