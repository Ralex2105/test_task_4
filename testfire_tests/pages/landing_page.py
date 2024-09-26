import logging
from selenium.webdriver.common.by import By

from framework.elements.textbox_element import TextBoxElement
from framework.elements.button_element import ButtonElement
from framework.pages.base_page import BasePage


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LandingPage(BasePage):
    """
    Landing page class with basic elements
    """

    SEARCH_PAGE_UNIQUE_ELEMENT_NAME = "search query textbox"
    SEARCH_PAGE_UNIQUE_ELEMENT_LOCATOR = (By.NAME, "query")

    __SEARCH_PAGE_SEARCH_TEXTBOX_NAME = "search_textbox_element"
    __SEARCH_PAGE_SEARCH_TEXTBOX_LOCATOR = (By.NAME, "query")

    __SEARCH_PAGE_SEARCH_BUTTON_NAME = "search_button_element"
    __SEARCH_PAGE_SEARCH_BUTTON_LOCATOR = (By.XPATH, "//input[@type='submit' and @value='Go']", "search_button_element")

    @property
    def search_textbox_element(self):
        """
        Initialize and cache __SEARCH_PAGE_SEARCH_TEXTBOX.

        :return: An instance of TextBoxElement __SEARCH_PAGE_SEARCH_TEXTBOX.
        """
        logger.debug("Get search textbox element.")
        return self.get_cached_element(
            self.__SEARCH_PAGE_SEARCH_TEXTBOX_NAME,
            lambda: TextBoxElement(self.__SEARCH_PAGE_SEARCH_TEXTBOX_LOCATOR, self.__SEARCH_PAGE_SEARCH_TEXTBOX_NAME)
        )

    @property
    def search_button_element(self):
        """
        Initialize and cache __SEARCH_PAGE_SEARCH_BUTTON.

        :return: An instance of TextBoxElement __SEARCH_PAGE_SEARCH_BUTTON.
        """
        logger.debug("Get search button element.")
        return self.get_cached_element(
            self.__SEARCH_PAGE_SEARCH_BUTTON_NAME,
            lambda: ButtonElement(self.__SEARCH_PAGE_SEARCH_BUTTON_LOCATOR, self.__SEARCH_PAGE_SEARCH_BUTTON_NAME)
        )

    def enter_search_query(self, browser, query):
        """
        Enters the username into the username field.

        :param browser: instance Browser
        :param query: string to enter to field
        """
        logger.debug(f"Enter search query: {query}")
        self.search_textbox_element.enter_text(browser, query)

    def submit_search(self, browser):
        """
        Clicks the search button to submit the search query.

        :param browser: instance Browser
        """
        logger.debug("Submit search query.")
        self.search_button_element.click(browser)
