import pytest

from app.src.client import Client
import config
import os

url = config.url
payload = config.payload
headers = config.headers
ttl = config.ttl

field_rate = config.field_rate

client = Client(url, payload, headers, ttl, field_rate)


def test_request_1():
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
    with pytest.raises(Exception):
        rate = client.get_rate('asdasda', 'USD', 2)


def test_input_data_2():
    with pytest.raises(Exception):
        rate = client.get_rate('USD', 'USD', -2)


def test_input_data_3():
    with pytest.raises(Exception):
        rate = client.get_rate('USD', 'USD', 'sadasda')


def test_input_data_4():
    with pytest.raises(Exception):
        rate = client.get_rate('USD', 'QWEE', 4)


def test_code_status():
    with pytest.raises(Exception):
        client = Client(url, payload, {}, ttl, field_rate)
        rate = client.get_rate('USD', 'USD', 4)
