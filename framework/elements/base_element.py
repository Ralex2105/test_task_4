import logging
from abc import ABC
from selenium.webdriver.remote.webelement import WebElement

from framework.browser.browser import Browser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseElement(ABC):

    def __init__(self, locator, name):
        """
        Initializes the element with the specified locator.

        :param locator: locator (For example, (By.ID, "uid")
        """
        self.locator = locator
        self.name = name
        logger.debug(f"Initialized BaseElement: {self.name} with locator: {self.locator}.")

    def element(self) -> WebElement:
        """
        Abstract property that should return the WebElement instance.
        """
        pass

    def click(self, browser):
        """
        Clicks on the element.

        :param browser: instance Browse to click the element
        """
        logger.debug(f"Click on element: {self.name} with locator: {self.locator}.")
        Browser.find_element(browser, self.locator[0], self.locator[1]).click()

    def is_element_displayed(self, browser) -> bool:
        """
        Checks if the element is displayed on the page.

        :param browser: Instance of the Browser class
        :return: Returns True if the element is found and displayed, otherwise False
        """
        element = Browser.find_element(browser, self.locator[0], self.locator[1])
        logger.debug(f"Element {self.name} with locator: {self.locator} displayed: {element.is_displayed()}")
        return element.is_displayed()
