import subprocess
import pytest

API_URL = "api.apilayer.com"


@pytest.fixture(scope="session")
def nmap_scan():
    """
    Pytest fixture to perform an Nmap scan on the specified API domain.

    Returns:
        str: The output of the Nmap scan, which includes information about open ports.
    """
    cmd = ["nmap", "-p-", API_URL]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


@pytest.fixture(scope="session")
def nuclei_scan():
    """
    Pytest fixture to perform a Nuclei scan on the specified API domain.

    Returns:
        str: The output of the Nuclei scan, which includes information about detected vulnerabilities.
    """
    cmd = ["nuclei", "-u", f"https://{API_URL}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def test_nmap_scan(nmap_scan):
    """
    Test to check if any open ports were found by the Nmap scan.

    Args:
        nmap_scan (str): The output of the Nmap scan provided by the `nmap_scan` fixture.

    Raises:
        AssertionError: If "open" is not found in the Nmap scan output.
    """
    assert "open" in nmap_scan, "No open ports found"
    print(f"Nmap scan result:\n{nmap_scan}")


def test_nuclei_scan(nuclei_scan):
    """
    Test to check if any vulnerabilities were found by the Nuclei scan.

    Args:
        nuclei_scan (str): The output of the Nuclei scan provided by the `nuclei_scan` fixture.

    Raises:
        AssertionError: If "No vulnerabilities found" is present in the Nuclei scan output.
    """
    assert "No vulnerabilities found" not in nuclei_scan, "Vulnerabilities found"
    print(f"Nuclei scan result:\n{nuclei_scan}")
