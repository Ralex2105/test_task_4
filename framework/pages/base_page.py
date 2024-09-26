import logging
from abc import ABC

from framework.cache.cache_element import CacheElement
from framework.elements.base_element import BaseElement

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage(ABC, CacheElement):
    """
    Base class for representing a page in the Page Object Model.
    """

    def __init__(self, page_name, unique_element_locator):
        """
        Initializes the BasePage with a name and a unique element locator.

        :param page_name: The name of the page.
        :param unique_element_locator: Locator for the unique element on the page.
        """
        super().__init__()
        self.page_name = page_name
        self.unique_element_locator = unique_element_locator
        logger.debug(f"Initialized BasePage: {self.page_name} with unique locator: {self.unique_element_locator}")

    def is_open(self, browser) -> bool:
        """
        Checks if the page is currently open in the browser by verifying the presence of the unique element.

        :param: browser: The browser instance
        :returns: True if the unique element is displayed, False otherwise
        """
        unique_element = BaseElement(self.unique_element_locator, 'unique_element')
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

