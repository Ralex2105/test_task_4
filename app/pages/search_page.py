from app.pages.base_page import BasePage
from app.config import Locators


class SearchPage(BasePage):

    def enter_search_query(self, query):
        """
        Enters a search query into the search box.

        :param query: Search query string
        """
        search_box = self.find_element(*Locators.SEARCH_PAGE_SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(query)

    def submit_search(self):
        """
        Clicks the search button to submit the search query.
        """
        search_button = self.find_element(*Locators.SEARCH_PAGE_SEARCH_BOX)
        search_button.submit()