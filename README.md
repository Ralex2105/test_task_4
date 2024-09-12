# Selenium Testing Project

## Overview

This project is a Selenium-based testing framework for testing web applications. 

It includes tests for login functionality and XSS vulnerabilities.

## Project Structure

- **`pages/`**: Contains Page Object Model (POM) classes for different pages.
  - `base_page.py`: Contains the base class for common page operations.
  - `login_page.py`: Contains the `LoginPage` class for interacting with the login page.
  - `search_page.py`: Contains the `SearchPage` class for interacting with the search page.
  
- **`factories/`**: Contains factory classes to create page objects.
  - `page_factory.py`: Provides methods to instantiate different page objects.

- **`webdriver/`**: Contains driver classes to create webdriver.
  - `webdriver_singleton.py`: Provides methods to instantiate webdriver.

- **`conftest.py`**: Configuration file for pytest fixtures and setup.

- **`tests/`**: Contains test cases.
  - `test_login.py`: Contains tests for the login functionality.
  - `test_search_xss.py`: Contains tests for checking XSS vulnerabilities.

- **`config.py`**: Configuration file containing locators, URLs, and test data.

## Prerequisites

- Python 3.6+
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (for Firefox)
- [Firefox Browser](https://www.mozilla.org/en-US/firefox/new/)
- [Selenium](https://pypi.org/project/selenium/)
- [pytest](https://pypi.org/project/pytest/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ralex2105/test_task_4.git
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

## Configuration

Edit the `config.py` file to update any necessary configuration values: URLs, usernames, passwords, locators.

## Running Tests

1. **Run the tests with pytest:**

   ```bash
   pytest

## Best Practices

- **Page Object Model:** Used to separate page-specific code from test logic.
- **Factory Pattern:** Used to create page objects. The `PageFactory` class provides methods to instantiate different page objects.
- **Singleton Pattern:** Ensures a single WebDriver instance across tests to avoid redundant browser instances.
- **Configuration Management:** Centralized in `config.py` to simplify updates and maintenance of locators, URLs, test data.
- **Logging:** Incorporated to track test execution, errors, and useful debug information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
