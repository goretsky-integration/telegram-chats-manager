import httpx
import pytest

import exceptions
import models
from database_api import DatabaseAPIService


@pytest.fixture
def assert_all_responses_were_requested() -> bool:
    return False


@pytest.mark.parametrize(
    'response_data',
    [
        {
            'is_end_of_list_reached': True,
            'telegram_chats': [{'chat_id': 1234, 'title': 'Alex'}],
        },
    ]
)
def test_database_api_service_get_telegram_chats_last_page(httpx_mock, response_data):
    httpx_mock.add_response(json=response_data, method='GET')
    expected = [models.TelegramChat.from_response_data(chat) for chat in response_data['telegram_chats']]

    with httpx.Client(base_url='http://localhost:8000') as client:
        database_api_service = DatabaseAPIService(api_client=client)
        assert database_api_service.get_telegram_chats() == expected


def test_database_api_service_get_telegram_chats_pagination(httpx_mock):
    is_last_page = False

    def get_response(request: httpx.Request):
        nonlocal is_last_page
        if is_last_page:
            return httpx.Response(status_code=200, json={
                'is_end_of_list_reached': True,
                'telegram_chats': [{'chat_id': 1234, 'title': 'Alex'}],
            })
        is_last_page = True
        return httpx.Response(status_code=200, json={
            'is_end_of_list_reached': False,
            'telegram_chats': [{'chat_id': 2345, 'title': 'Steve'}],
        })

    httpx_mock.add_callback(get_response)
    expected = [models.TelegramChat.from_response_data(chat) for chat in
                [{'chat_id': 2345, 'title': 'Steve'}, {'chat_id': 1234, 'title': 'Alex'}]]

    with httpx.Client(base_url='http://localhost:8000') as client:
        database_api_service = DatabaseAPIService(api_client=client)
        assert database_api_service.get_telegram_chats() == expected


def test_database_api_service_raises_error(httpx_mock):
    httpx_mock.add_response(status_code=400)

    with httpx.Client(base_url='http://localhost:8000') as client:
        database_api_service = DatabaseAPIService(api_client=client)

        with pytest.raises(exceptions.DatabaseAPIError) as error:
            database_api_service.get_telegram_chats()
        assert error.value.args[0] == 'Could not get telegram chats page'
