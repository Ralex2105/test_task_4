# Exchange Rate Converter

This library provides utilities for interacting with APIs, including caching responses and handling requests.
This library includes three main entities: client, cache, API

## Classes

### `Cache`

Manages temporary storage of data with a time-to-live (TTL) setting.

- **Initialize**: `Cache(ttl, not_found_obj=None)`
- **Set Data**: `cache.set(key, value)`
- **Get Data**: `cache.get(key)`

### `Client`

Handles API interactions, caching, and processing of exchange rate data.

- **Initialize**: `Client(url, payload, headers, ttl, field_rate)`
- **Get Rate**: `client.get_rate(value_1, value_2, amount)`

### `API`

Sends HTTP requests to an API endpoint.

- **Initialize**: `API(url, payload, headers)`
- **Request**: `api.request()`

## Usage

1. **Cache**: Use to cache API responses to reduce redundant requests.
2. **Client**: Interact with the API, leveraging the `Cache` for efficiency.
3. **API**: Directly send requests to the API and handle responses.

To use the library, you need parameters that must be passed when initializing the client object: url, headers, payload, ttl, field_rate:

1. **URL**: The API endpoint URL.
2. **PAYLOAD**: The payload to be sent with the API request.
3. **HEADERS**: The headers to be sent with the API request.
4. **TTL**: Time-to-live for caching API responses.
5. **Field_rate**: The key in the API response containing the exchange rate data.

## Example usage
```
url = "https://api.apilayer.com/exchangerates_data/latest"
payload = {}
headers = {"apikey": "apikey"}
ttl = 3600
field_rate = 'rates'

client = Client(url, payload, headers, ttl, field_rate)
rate = client.get_rate('USD', 'USD', 4)
```

## Project cloning
```git clone https://github.com/Ralex2105/test_task_4.git -b develop/task_4```


## Testing
Several smoke tests have been written for this application. Testing covers basic functionality and correctness of input data.
To run tests you must use:
```
cd test_task_4
docker-compose run pytest
```

# Testing (additional task)
As an additional task, tests were written using the nmap and nuclei utilities

## Project cloning
```git clone https://github.com/Ralex2105/test_task_4.git -b develop/task_4```

## Testing
1. Tests if the SSL certificate is valid.
To run tests you must use:
```
cd test_task_4
docker-compose run cert
```

2.1. Test to check if any vulnerabilities were found by the Nuclei scan.

2.2. Test to check if any open ports were found by the Nmap scan.
```
cd test_task_4
docker-compose run nmap
```
To run all tests
```
docker-compose up --build
```

## For local tests
Check actual version of nmap, pytest, nuclei and run tests:
```
nuclei --version
nmap --version 
pytest --version
```
