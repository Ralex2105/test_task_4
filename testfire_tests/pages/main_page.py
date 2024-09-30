import logging
from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from framework.elements.button_element import ButtonElement

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MainPage(BasePage):
    """
    Main page class with basic elements
    """
    __PAGE_NAME = "main page"

    __UNIQUE_ELEMENT_NAME = "unique element"
    __UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//a[font[text()='Sign Off']]")

    def __init__(self):
        """
        Initializes the MainPage with a name and a unique element locator.
        """
        self.unique_element = ButtonElement(self.__UNIQUE_ELEMENT_LOCATOR, self.__UNIQUE_ELEMENT_NAME)
        super().__init__(self.__PAGE_NAME, self.unique_element)

    def page_specific_method(self):
        """
        Implement specific abstract method
        """
        pass
