import ssl
import socket
import pytest
from datetime import datetime


API_DOMAIN = "api.apilayer.com"
API_PORT = 443


@pytest.fixture
def ssl_certificate():
    """
    Pytest fixture that retrieves the SSL certificate from the API domain.

    Returns:
        dict: A dictionary containing the SSL certificate information.
    """
    context = ssl.create_default_context()

    with socket.create_connection((API_DOMAIN, API_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=API_DOMAIN) as ssock:
            certificate = ssock.getpeercert()
            return certificate


@pytest.fixture
def current_time():
    """
    Pytest fixture that provides the current UTC time.

    Returns:
        datetime: The current time in UTC.
    """
    return datetime.utcnow()


def test_valid_certificate(ssl_certificate, current_time):
    """
    Tests if the SSL certificate is valid.

    Args:
        ssl_certificate (dict): The SSL certificate retrieved by the fixture.
        current_time (datetime): The current UTC time provided by the fixture.
    """
    assert ssl_certificate is not None, "Failed to retrieve the cert"

    not_before = datetime.strptime(ssl_certificate['notBefore'], '%b %d %H:%M:%S %Y %Z')
    not_after = datetime.strptime(ssl_certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')

    assert not_before <= current_time <= not_after, "The certificate is not valid."
    print(f"The certificate is valid from {not_before} to {not_after}.")


def test_certificate_subject(ssl_certificate):
    """
    Tests if the SSL certificate is issued for the correct domain.

    Args:
        ssl_certificate (dict): The SSL certificate retrieved by the fixture.
    """
    assert ssl_certificate is not None, "Failed to retrieve the certificate."

    subject = dict(x[0] for x in ssl_certificate['subject'])

    assert subject[
               'commonName'] == API_DOMAIN, \
        f"The certificate was issued for {subject['commonName']} instead of {API_DOMAIN}."
    print(f"The certificate is issued for {subject['commonName']}.")