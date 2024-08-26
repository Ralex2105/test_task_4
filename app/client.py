import json


from app.api import API
from app.cache import Cache
from app.AppException import IncorrectInputData, IncorrectReceivedData, CodeStatusError


class Client:
    """
    A client for interacting with an external API to retrieve and process exchange rates.

    Attributes:
        url (str): The API endpoint URL.
        payload (dict): The payload to be sent with the API request.
        headers (dict): The headers to be sent with the API request.
        ttl (int): Time-to-live for caching API responses.
        field_rate (str): The key in the API response containing the exchange rate data.
        cache (Cache): An instance of the Cache class to store and retrieve cached data.
        request (API): An instance of the API class to handle API requests.
    """

    def __init__(self, url, payload, headers, ttl, field_rate):
        """
        Initializes the Client with API details and cache settings.

        Args:
            url (str): The URL of the API endpoint.
            payload (dict): The data to be sent in the request body.
            headers (dict): The headers to include in the API request.
            ttl (int): The time-to-live in seconds for cached API responses.
            field_rate (str): The field in the API response that contains the exchange rates.
        """
        self.url = url
        self.payload = payload
        self.headers = headers
        self.ttl = ttl

        self.field_rate = field_rate

        self.cache = Cache(self.ttl)
        self.request = API(self.url, self.payload, self.headers)

    def get_rate(self, value_1, value_2, amount):
        """
        Retrieves the exchange rate between two currencies for a given amount.

        Args:
            value_1 (str): The source currency code.
            value_2 (str): The target currency code.
            amount (int): The amount to convert from `value_1` to `value_2`.

        Returns:
            float: The calculated exchange rate for the given amount.

        Raises:
            CodeStatusError: If the API returns an unexpected HTTP status code.
            IncorrectReceivedData: If the received data is missing expected fields.
            IncorrectInputData: If the input data is invalid (e.g., negative amount).
        """
        try:
            received_data = self.__get_actual_data()

            parse_received_data = self.__parse_received_data(received_data, self.field_rate)

            rate = self.__check_values_and_get_rate(parse_received_data, value_1, value_2, amount)

        except CodeStatusError:
            raise CodeStatusError
        except IncorrectReceivedData:
            raise IncorrectReceivedData
        except IncorrectInputData:
            raise IncorrectInputData

        return rate

    def __get_actual_data(self):
        """
        Retrieves the latest data from the cache or makes a new API request.

        Returns:
            str: The raw data received from the API or cache.

        Raises:
            CodeStatusError: If the API returns an unexpected HTTP status code.
        """
        if self.cache.get(self.url) is None:
            received_data, status_code = self.request.request()
            if status_code == 200:
                self.cache.set(self.url, received_data)
                return received_data
            else:
                raise CodeStatusError
        else:
            received_data = self.cache.get(self.url)
            return received_data

    def __parse_received_data(self, received_data, field_rate):
        """
        Parses the received data from the API to extract the exchange rate information.

        Args:
            received_data (str): The raw JSON data received from the API or cache.
            field_rate (str): The key to look for in the JSON data that contains the rates.

        Returns:
            dict: The parsed exchange rate data.

        Raises:
            IncorrectReceivedData: If the expected field is not found in the JSON data.
         """
        json_received_data = json.loads(received_data)
        if field_rate not in json_received_data:
            raise IncorrectReceivedData
        else:
            parse_received_data = json_received_data[field_rate]
            return parse_received_data

    def __check_values_and_get_rate(self, parse_received_data, value_1, value_2, amount):
        """
        Validates the input values and calculates the exchange rate.

        Args:
            parse_received_data (dict): The parsed exchange rate data.
            value_1 (str): The source currency code.
            value_2 (str): The target currency code.
            amount (int): The amount to convert from `value_1` to `value_2`.

        Returns:
            float: The calculated exchange rate for the given amount.

        Raises:
            IncorrectInputData: If the input currency codes or amount are invalid.
        """
        if not isinstance(amount, int) or amount < 0:
            raise IncorrectInputData

        if value_1 not in parse_received_data or value_2 not in parse_received_data:
            raise IncorrectInputData

        base_to_value_1 = parse_received_data[value_1]
        base_to_value_2 = parse_received_data[value_2]

        value_1_to_base = 1 / base_to_value_1
        rate = value_1_to_base * base_to_value_2 * amount

        return rate
