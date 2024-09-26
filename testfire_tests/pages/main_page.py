import logging
from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MainPage(BasePage):
    """
    Main page class with basic elements
    """

    MAIN_PAGE_UNIQUE_ELEMENT_NAME = "main page unique element"
    MAIN_PAGE_UNIQUE_ELEMENT_LOCATOR = (By.XPATH, "//a[font[text()='Sign Off']]")
