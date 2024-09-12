from app.pages.login_page import LoginPage
from app.pages.search_page import SearchPage


class PageFactory:
    @staticmethod
    def create_login_page(driver):
        """
        Creates an instance of LoginPage.

        :param driver: WebDriver instance
        :return: LoginPage instance
        """
        return LoginPage(driver)

    @staticmethod
    def create_search_page(driver):
        """
        Creates an instance of SearchPage.

        :param driver: WebDriver instance
        :return: SearchPage instance
        """
        return SearchPage(driver)