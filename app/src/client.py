import json


from app.src.api import API
from app.src.cache import Cache
from app.src.AppException import IncorrectInputData, IncorrectReceivedData, CodeStatusError


class Client:

    def __init__(self, url, payload, headers, ttl, field_rate):
        self.url = url
        self.payload = payload
        self.headers = headers
        self.ttl = ttl

        self.field_rate = field_rate

        self.cache = Cache(self.ttl)
        self.request = API(self.url, self.payload, self.headers)

    def get_rate(self, value_1, value_2, amount):

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
        json_received_data = json.loads(received_data)
        if field_rate not in json_received_data:
            raise IncorrectReceivedData
        else:
            parse_received_data = json_received_data[field_rate]
            return parse_received_data

    def __check_values_and_get_rate(self, parse_received_data, value_1, value_2, amount):
        if not isinstance(amount, int) or amount < 0:
            raise IncorrectInputData

        if value_1 not in parse_received_data or value_2 not in parse_received_data:
            raise IncorrectInputData

        base_to_value_1 = parse_received_data[value_1]
        base_to_value_2 = parse_received_data[value_2]

        value_1_to_base = 1 / base_to_value_1
        rate = value_1_to_base * base_to_value_2 * amount

        return rate
