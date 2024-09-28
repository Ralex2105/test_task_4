import logging
from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MainPage(BasePage):
    """
    Main page class with basic elements
    """

    __PAGE_NAME = "main page"
    __UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//a[font[text()='Sign Off']]")

    def __init__(self):
        """
        Initializes the MainPage with a name and a unique element locator.
        """
        super().__init__(self.__PAGE_NAME, self.__UNIQUE_ELEMENT_LOCATOR)
