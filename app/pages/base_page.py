from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        Initializes the BasePage with a WebDriver instance and timeout.

        :param driver: WebDriver instance
        :param timeout: Timeout for waits in seconds
        """
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, by: By, value: str):
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

    def wait_for_alert(self):
        """
        Waits for an alert to be present.

        :return: Alert instance
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()
        )

    def get_element_text(self, by: By, value: str):
        """
        Retrieves the text of an element.

        :param by: Locator strategy
        :param value: Locator value
        :return: Text of the WebElement
        """
        element = self.find_element(by, value)
        return element.text

    def click_element(self, by: By, value: str):
        """
        Clicks on an element.

        :param by: Locator strategy
        :param value: Locator value
        """
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by: By, value: str, text: str):
        """
        Enters text into an input field.

        :param by: Locator strategy
        :param value: Locator value
        :param text: Text to be entered
        """
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def navigate_to(self, url: str):
        """
        Navigates to a given URL.

        :param url: URL to navigate to
        """
        self.driver.get(url)
