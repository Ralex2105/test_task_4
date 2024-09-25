import logging
from selenium.webdriver.common.by import By

from framework.elements.textbox_element import TextBoxElement
from framework.elements.button_element import ButtonElement
from framework.pages.base_page import BasePage
from framework.cache.cache_element import CacheElement


class LandingPage(BasePage, CacheElement):
    """
    Landing page class with basic elements
    """

    __SEARCH_PAGE_SEARCH_TEXTBOX_NAME = "search_textbox_element"
    __SEARCH_PAGE_SEARCH_TEXTBOX = (By.NAME, "query")

    __SEARCH_PAGE_SEARCH_BUTTON_NAME = "search_button_element"
    __SEARCH_PAGE_SEARCH_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Go']", "search_button_element")

    @property
    def search_textbox_element(self):
        """
        Initialize and cache __SEARCH_PAGE_SEARCH_TEXTBOX.

        :return: An instance of TextBoxElement __SEARCH_PAGE_SEARCH_TEXTBOX.
        """
        logging.debug("Get search textbox element.")
        return self.get_cached_element(
            self.__SEARCH_PAGE_SEARCH_TEXTBOX_NAME,
            lambda: TextBoxElement(self.__SEARCH_PAGE_SEARCH_TEXTBOX, self.__SEARCH_PAGE_SEARCH_TEXTBOX_NAME)
        )

    @property
    def search_button_element(self):
        """
        Initialize and cache __SEARCH_PAGE_SEARCH_BUTTON.

        :return: An instance of TextBoxElement __SEARCH_PAGE_SEARCH_BUTTON.
        """
        logging.debug("Get search button element.")
        return self.get_cached_element(
            self.__SEARCH_PAGE_SEARCH_BUTTON_NAME,
            lambda: ButtonElement(self.__SEARCH_PAGE_SEARCH_BUTTON, self.__SEARCH_PAGE_SEARCH_BUTTON_NAME)
        )

    def enter_search_query(self, browser, query):
        """
        Enters the username into the username field.

        :param browser: instance Browser
        :param query: string to enter to field
        """
        logging.debug(f"Enter search query: {query}")
        self.search_textbox_element.enter_text(browser, query)

    def submit_search(self, browser):
        """
        Clicks the search button to submit the search query.

        :param browser: instance Browser
        """
        logging.debug("Submit search query.")
        self.search_button_element.click(browser)
