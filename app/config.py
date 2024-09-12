from selenium.webdriver.common.by import By


class Locators:
    """
    Class to store locators for different pages.
    """
    # Login Page
    LOGIN_PAGE_USERNAME_FIELD = (By.ID, "uid")
    LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "passw")
    LOGIN_PAGE_LOGIN_BUTTON = (By.NAME, "btnSubmit")

    # Search Page
    SEARCH_PAGE_SEARCH_BOX = (By.NAME, "query")


class URLs:
    """
    Class to store URLs for the application and test-specific URLs.
    """
    BASE_URL = "http://testfire.net"
    LOGIN_URL_BEFORE_AUTH = f"{BASE_URL}/login.jsp"
    LOGIN_URL_AFTER_AUTH = f"{BASE_URL}/bank/main.jsp"


class Credentials:
    """
    Class to store login credentials for testing.
    """
    USERNAME = "admin"
    PASSWORD = "admin"


class TestData:
    """
    Class to store test-specific data such as XSS payloads.
    """
    XSS_PAYLOAD = "<script>alert('XSS')</script>"
