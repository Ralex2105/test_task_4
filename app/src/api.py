import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    @abstractmethod
    def request(self):
        pass


class API(AbstractAPI):

    def __init__(self, url, payload, headers):
        self.url = url
        self.payload = payload
        self.headers = headers

    def request(self):
        response = requests.request("GET", url=self.url, headers=self.headers, data=self.payload)
        status_code = response.status_code
        result = response.text
        return result, status_code
