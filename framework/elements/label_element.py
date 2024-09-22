from framework.elements.base_element import BaseElement
from framework.browser.browser import Browser


class LabelElement(BaseElement):

    def enter_text(self, browser, word):
        """
        Enter text to label element

        :param browser: instance Browser
        :param word: word to enter
        """
        Browser.find_element(browser, self.locator[0], self.locator[1]).send_keys(word)

    def clean(self, browser):
        """
        Clear the filed from values

        :param browser: instance Browser
        """
        Browser.find_element(browser, self.locator[0], self.locator[1]).clear()
