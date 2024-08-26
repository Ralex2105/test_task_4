import pytest

from app.client import Client
from app.test import config
import os

url = config.url
payload = config.payload
headers = config.headers
ttl = config.ttl

field_rate = config.field_rate

client = Client(url, payload, headers, ttl, field_rate)


def test_request_1():
    """
    Test to verify the correct functionality of the 'get_rate' method in the Client class.

    The test performs the following steps:
    1. Retrieves the rate for 'USD' to 'USD' and asserts it is a float.
    2. Retrieves the rate for 'ALL' to 'USD' and asserts it is a float after disabling the network.
    """
    rate = client.get_rate('USD', 'USD', 4)
    assert isinstance(rate, float)
    rate = client.get_rate('USD', 'USD', 4)
    assert isinstance(rate, float)
    os.environ["PYTEST_DISABLE_NETWORK"] = "1"
    rate = client.get_rate('ALL', 'USD', 4)
    assert isinstance(rate, float)
    rate = client.get_rate('EUR', 'USD', 4)
    assert isinstance(rate, float)
    os.environ["PYTEST_DISABLE_NETWORK"] = "0"


def test_request_2():
    """
    Test to verify the correct functionality of the 'get_rate' method under repeated requests more than 100 times..

    The test performs the following steps:
    1. Retrieves the rate for 'USD' to 'USD' and asserts it is a float.
    2. Disables the network and performs multiple requests with different currency pairs.
    """
    rate = client.get_rate('USD', 'USD', 4)
    assert isinstance(rate, float)
    os.environ["PYTEST_DISABLE_NETWORK"] = "1"
    for i in range(110):
        rate = client.get_rate('GBP', 'ALL', 4)
        assert isinstance(rate, float)
        rate = client.get_rate('USD', 'EUR', 4)
        assert isinstance(rate, float)
    os.environ["PYTEST_DISABLE_NETWORK"] = "0"


def test_input_data_1():
    """
    Test to verify that the 'get_rate' method raises an exception for invalid base currency input.

    This test checks if an exception is raised when an invalid base currency is provided to the `get_rate` method.
    """
    with pytest.raises(Exception):
        rate = client.get_rate('asdasda', 'USD', 2)


def test_input_data_2():
    """
    Test to verify that the 'get_rate' method raises an exception for invalid amount input.

    """
    with pytest.raises(Exception):
        rate = client.get_rate('USD', 'USD', -2)


def test_input_data_3():
    with pytest.raises(Exception):
        """
        Test to verify that the 'get_rate' method raises an exception for invalid amount input.

        """
        rate = client.get_rate('USD', 'USD', 'sadasda')


def test_input_data_4():
    """
    Test to verify that the 'get_rate' method raises an exception for invalid amount input.

    """
    with pytest.raises(Exception):
        rate = client.get_rate('USD', 'QWEE', 4)


def test_code_status():
    """
    Test to verify that the 'get_rate' method raises an exception for invalid amount input.

    """
    with pytest.raises(Exception):
        client = Client(url, payload, {}, ttl, field_rate)
        rate = client.get_rate('USD', 'USD', 4)
