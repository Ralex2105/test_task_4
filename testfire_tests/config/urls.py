class URLs:
    """
    Class to store URLs for the application and test-specific URLs.
    """
    BASE_URL = "http://testfire.net"
    LOGIN_URL_BEFORE_AUTH = f"{BASE_URL}/login.jsp"
    LOGIN_URL_AFTER_AUTH = f"{BASE_URL}/bank/main.jsp"
