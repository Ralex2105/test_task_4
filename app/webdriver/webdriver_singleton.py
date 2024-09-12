from selenium import webdriver


class WebDriverSingleton:
    _driver = None

    @staticmethod
    def get_driver():
        """
        Gets the webdriver instance.

        :return: WebDriver instance
        """
        if WebDriverSingleton._driver is None:
            WebDriverSingleton._driver = webdriver.Firefox()
        return WebDriverSingleton._driver

    @staticmethod
    def quit_driver():
        """
        Quits the webdriver instance.
        """
        if WebDriverSingleton._driver is not None:
            WebDriverSingleton._driver.quit()
            WebDriverSingleton._driver = None
