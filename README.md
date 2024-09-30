# Selenium Testing Project

## Overview

This project is a Selenium-based testing framework for testing web applications. 

It includes tests for login functionality and XSS vulnerabilities.

## Project Structure

1. **`framework/`**

   - **`browser/`**
     - `browser.py`: This module handles the initialization and configuration of the browser for Selenium testing.
     - `browser_factory.py`: This module follows the Factory design pattern to create and return the appropriate browser instance.
     - `singleton.py`: This module ensures that only one instance of the browser is created using the Singleton pattern.
     
   - **`cache/`**
     - `cache_element.py`: This module is responsible for caching web elements that are frequently used during testing.
     
   - **`config/`**
     - `driver_list.py`: This module provides a list of supported WebDriver instances (Chrome, Firefox, etc.).
     - `test_data.py`: This module stores test data such as URLs, login credentials, and other static information needed for tests.
     
   - **`elements/`**
     - `base_element.py`: This is the base class for all web elements used in the page object model (POM).
     - `button_element.py`: This module represents a button element in the POM.
     - `label_element.py`: This module represents a label element in the POM.
     - `textbox_element.py`: This module represents a textbox element in the POM.
     
   - **`pages/`**
     - `base_page.py`: This is the base class for all page objects in the page object model (POM).

2. testfire_tests

    - **`config/`**
     - `credentials.py`: This module stores sensitive login credentials (e.g., usernames and passwords) for automated tests.
     - `urls.py`: This module contains a list of URLs.
   - **`pages/`**
     - `landing_page.py`: This module defines the page object for the landing page.
     - `login_page.py`: This module defines the page object for the login page.
     - `main_page.py`: This module defines the page object for the main/home page after successful login.
   - **`tests/`**
     - `conftests.py`: This module contains shared fixtures and configuration for the test suite.
     - `test_login.py`: This test module contains test cases for the login functionality.
     - `test_search_xss.py`: This test module is focused on verifying that the search functionality is secure against XSS attacks.
     

## Prerequisites

- Python 3.6+
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (for Firefox)
- [MSEdgeDriver](ttps://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (For Edge)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (For Chrome)
- [Firefox Browser](https://www.mozilla.org/en-US/firefox/new/)
- [Selenium](https://pypi.org/project/selenium/)
- [pytest](https://pypi.org/project/pytest/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ralex2105/test_task_4.git -b develop/task_2
   cd test_task_4

2. **Create a virtual environment:**

   ```bash
   python -m venv venv

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt

5. **Download GeckoDriver:**
   - Download the appropriate version for your operating system from [here](https://github.com/mozilla/geckodriver/releases).
   - Extract the downloaded file and add `geckodriver` to your system’s PATH.
   
   **Download EdgeDriver:**
   - Download the appropriate version for your operating system from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
   - Extract the downloaded file and add `msedgedriver` to your system’s PATH.
   
   **Download ChromeDriver:**
   - Download the appropriate version for your operating system from [here](https://sites.google.com/chromium.org/driver/)
   - Extract the downloaded file and add `chromedriver` to your system’s PATH.

## Configuration

Edit environments and include:

    LOGIN_USERNAME = ""
    LOGIN_PASSWORD = ""

## Running Tests

1. **Run the tests with pytest:**

   ```bash
   pytest

## Best Practices

- **Page Object Model:** Used to separate page-specific code from test logic.
- **Factory Pattern:** Used to create browser (Chrome, Firefox, etc.).
- **Singleton Pattern:** Ensures a single WebDriver instance across tests to avoid redundant browser instances.
- **Configuration Management:** Centralized in `config.py` to simplify updates and maintenance of locators, URLs, test data.
- **Logging:** Incorporated to track test execution, errors, and useful debug information.

## License
This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
