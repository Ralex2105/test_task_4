import logging

from framework.elements.base_element import BaseElement
from framework.browser.browser import Browser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LabelElement(BaseElement):

    def get_text(self, browser):
        """
        Get text from label element

        :param browser: instance Browser
        """
        logger.debug(f"Get text from label element: {self.name} with locator: {self.locator}.")
        Browser.find_element(browser, self.locator[0], self.locator[1]).text()
