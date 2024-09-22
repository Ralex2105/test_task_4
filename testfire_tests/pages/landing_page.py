from selenium.webdriver.common.by import By

from framework.elements.textbox_element import TextBoxElement
from framework.pages.base_page import BasePage


class LandingPage(BasePage):
    """
    Landing page class with basic elements
    """

    __SEARCH_PAGE_SEARCH_BOX = (By.NAME, "query")

    def __init__(self):
        """
        Initializing the landing page with basic elements
        """
        self.search_box_element = TextBoxElement(self.__SEARCH_PAGE_SEARCH_BOX)

    def enter_search_query(self, browser, query):
        """
        Enters the username into the username field.

        :param browser: instance Browser
        :param query: string to enter to field
        """
        self.search_box_element.enter_text(browser, query)

    def submit_search(self, browser):
        """
        Clicks the search button to submit the search query.

        :param browser: instance Browser
        """
        self.search_box_element.click(browser)
