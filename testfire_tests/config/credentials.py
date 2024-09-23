import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:
    """
    Class to store Credentials for the testing.
    """
    LOGIN_USERNAME = os.getenv("LOGIN_USERNAME")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
