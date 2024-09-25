import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserFactory(object):

    def initialize_browser(browser_type: str):
        """
        Initializes the WebDriver instance based on the browser type.

        :param browser_type: Browser type ('chrome', 'firefox')
        """
        logging.debug(f"Initialize browser of type: {browser_type} in BrowserFactory.")

        if browser_type == 'chrome':
            chrome_options = ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            service = Service(executable_path='/path/to/chromedriver')
            logging.debug("Initialize Chrome.")
            return webdriver.Chrome(service=service, options=chrome_options)

        elif browser_type == 'firefox':
            firefox_options = FirefoxOptions()
            service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
            logging.debug("Initialize FireFox.")
            return webdriver.Firefox(service=service, options=firefox_options)

        elif browser_type == 'edge':
            edge_options = EdgeOptions()
            edge_options.add_argument('--start-maximized')
            service = EdgeService(executable_path='/path/to/msedgedriver')
            logging.debug("Initialize Edge.")
            return webdriver.Edge(service=service, options=edge_options)

        else:
            logging.error(f"Unsupported browser type: {browser_type}")
            raise ValueError(f"Browser type {browser_type} is not supported.")


