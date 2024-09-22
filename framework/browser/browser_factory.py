from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserFactory:
    """

    """
    _instance = None
    _driver = None

    def __new__(cls, browser_type: str = 'chrome'):
        """
        Implements Singleton pattern to ensure only one instance of WebDriver is created.

        :param browser_type: Browser type ('chrome', 'firefox')
        :return: BrowserFactorySingleton instance
        """
        if cls._instance is None:
            cls._instance = super(BrowserFactory, cls).__new__(cls)
            cls._instance._initialize_browser(browser_type)
        return cls._instance

    def _initialize_browser(self, browser_type: str):
        """
        Initializes the WebDriver instance based on the browser type.

        :param browser_type: Browser type ('chrome', 'firefox')
        """
        if browser_type == 'chrome':
            chrome_options = ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            service = Service(executable_path='/path/to/chromedriver')
            self._driver = webdriver.Chrome(service=service, options=chrome_options)
        elif browser_type == 'firefox':
            firefox_options = FirefoxOptions()
            service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
            self._driver = webdriver.Firefox(service=service, options=firefox_options)
        elif browser_type == 'edge':
            edge_options = EdgeOptions()
            edge_options.add_argument('--start-maximized')
            service = EdgeService(executable_path='/path/to/msedgedriver')
            self._driver = webdriver.Edge(service=service, options=edge_options)
        else:
            raise ValueError(f"Browser type {browser_type} is not supported.")

    @property
    def driver(self):
        """
        Returns the WebDriver instance.
        """
        return self._driver

    def close_browser(self):
        """
        Closes the browser and quits the WebDriver session.
        """
        if self._driver:
            self._driver.quit()
            BrowserFactory._instance = None

    def change_browser_type(self, new_browser_type: str):
        """
        Changes the browser type by initializing a new WebDriver instance.

        :param new_browser_type: New browser type ('chrome', 'firefox')
        """
        self._initialize_browser(new_browser_type)
