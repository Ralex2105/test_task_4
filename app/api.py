import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Abstract base class for making API requests.
    """

    @abstractmethod
    def request(self):
        """
        Abstract method for making an API request.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        pass


class API(AbstractAPI):
    """
    A concrete implementation of the AbstractAPI class for making HTTP GET requests.
    """

    def __init__(self, url, payload, headers):
        """
        Initializes the API object with the necessary parameters for making a request.

        Args:
            url (str): The URL to which the GET request will be sent.
            payload (dict or None): The data to be sent in the body of the request.
            headers (dict): The headers to be sent with the request (ApiToken).
        """
        self.url = url
        self.payload = payload
        self.headers = headers

    def request(self):
        """
        Sends a GET request to the specified URL with the given headers and payload.

        Returns:
            tuple: A tuple containing the response text and the HTTP status code.
        """
        response = requests.request("GET", url=self.url, headers=self.headers, data=self.payload)
        status_code = response.status_code
        result = response.text
        return result, status_code
