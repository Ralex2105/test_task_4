import logging
from abc import ABC, abstractmethod

from framework.cache.cache_element import CacheElement

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage(ABC, CacheElement):
    """
    Base class for representing a page in the Page Object Model.
    """

    def __init__(self, page_name, unique_element):
        """
        Initializes the BasePage with a name and a unique element locator.

        :param page_name: The name of the page.
        :param unique_element: Unique element on the page.
        """
        super().__init__()
        self.page_name = page_name
        self.unique_element = unique_element
        logger.debug(f"Initialized BasePage: {self.page_name} with unique element: {self.unique_element}")

    def is_open(self, browser) -> bool:
        """
        Checks if the page is currently open in the browser by verifying the presence of the unique element.

        :param: browser: The browser instance
        :returns: True if the unique element is displayed, False otherwise
        """
        unique_element = self.unique_element
        unique_element_is_displayed = unique_element.is_element_displayed(browser)
        logger.debug(f"Unique element of {self.page_name} is displayed: {unique_element_is_displayed}.")
        return unique_element_is_displayed

    def get_page_name(self):
        """
        Retrieves the name of the page.

        :returns: The name of the page
        """
        logger.debug(f"Retrieving page name: {self.page_name}")
        return self.page_name

    def reset_element_cache(self, name=None):
        """
        Resets the element cache for the page.

        :param name: The name of the specific element cache to reset. Defaults to None,
                                  which resets all cached elements.
        """
        if name:
            logger.info(f"Resetting cache for element: {name} on page '{self.page_name}'")
        else:
            logger.info(f"Resetting cache for all elements on page '{self.page_name}'")
        super().reset_element_cache(name)

    @abstractmethod
    def page_specific_method(self):
        """
        Abstract method to implement in subclasses
        """
        pass
