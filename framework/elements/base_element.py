import logging
from abc import ABC
from selenium.webdriver.remote.webelement import WebElement

from framework.browser.browser import Browser


class BaseElement(ABC):

    def __init__(self, locator, name):
        """
        Initializes the element with the specified locator.

        :param locator: locator (For example, (By.ID, "uid")
        """
        self.locator = locator
        self.name = name
        logging.debug(f"Initialized BaseElement: {self.name} with locator: {self.locator}.")

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
        logging.debug(f"Click on element: {self.name} with locator: {self.locator}.")
        Browser.find_element(browser, self.locator[0], self.locator[1]).click()
