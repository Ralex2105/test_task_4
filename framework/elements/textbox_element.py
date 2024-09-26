import logging

from framework.elements.base_element import BaseElement
from framework.browser.browser import Browser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextBoxElement(BaseElement):

    def enter_text(self, browser, word):
        """
        Enter text to textbox element

        :param browser: instance Browser
        :param word: word to enter
        """
        logger.debug(f"Enter text {word} into text box: {self.name} with locator: {self.locator}.")
        Browser.find_element(browser, self.locator[0], self.locator[1]).send_keys(word)

    def clean(self, browser):
        """
        Clear the filed from values

        :param browser: instance Browser
        """
        logger.debug(f"Clear text box: {self.name} with locator: {self.locator}.")
        Browser.find_element(browser, self.locator[0], self.locator[1]).clear()
