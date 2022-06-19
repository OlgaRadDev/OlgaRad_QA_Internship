import pytest

from tests.http import HttpClient

@pytest.fixture(scope="session")
def http_client():
    yield HttpClient("https://gorest.co.in", 'b14c79b1541e7791428d4af9470e46bc7d3e4e4c3e13a43df12e915282a23237')



