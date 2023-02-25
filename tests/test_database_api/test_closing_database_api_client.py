import pytest

from database_api import closing_database_api_client


@pytest.mark.parametrize(
    'base_url',
    [
        'http://localhost:8000/',
        'http://localhost:7050/',
    ]
)
def test_closing_database_api_client(base_url: str):
    with closing_database_api_client(base_url=base_url) as client:
        assert client.base_url == base_url
