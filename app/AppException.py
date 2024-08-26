class CodeStatusError(Exception):
    """
    Exception raised when an unexpected HTTP status code is received from an API request.
    """
    pass


class IncorrectReceivedData(Exception):
    """
    Exception raised when the data received from an API request is incorrect or malformed.
    """
    pass


class IncorrectInputData(Exception):
    """
    Exception raised when the input data provided to a function or API request is invalid.
    """
    pass
