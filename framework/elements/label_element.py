import logging

from framework.elements.base_element import BaseElement
from framework.browser.browser import Browser


class LabelElement(BaseElement):

    def get_text(self, browser):
        """
        Get text from label element

        :param browser: instance Browser
        """
        logging.debug(f"Get text from label element: {self.name} with locator: {self.locator}.")
        Browser.find_element(browser, self.locator[0], self.locator[1]).text()
