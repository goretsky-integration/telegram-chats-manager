import httpx
import pytest

import exceptions
import models
from telegram import TelegramAPIService


@pytest.fixture
def telegram_api_service():
    with httpx.Client(base_url='http://localhost:8000') as client:
        yield TelegramAPIService(api_client=client)


@pytest.mark.parametrize(
    'response_json, chat',
    [
        (
                {
                    'result': {
                        'id': 1234,
                        'type': 'private',
                        'first_name': 'Alex',
                    }
                },
                models.Chat(
                    id=1234,
                    type='private',
                    first_name='Alex',
                ),
        ),
        (
                {
                    'result': {
                        'id': 1234,
                        'type': 'supergroup',
                        'title': 'Managers',
                        'username': 'managers',
                    }
                },
                models.Chat(
                    id=1234,
                    type='supergroup',
                    title='Managers',
                    username='managers',
                ),
        ),
    ]
)
def test_telegram_api_service_get_chats(httpx_mock, telegram_api_service, response_json, chat):
    httpx_mock.add_response(json=response_json)
    assert telegram_api_service.get_chat(chat_id=1234) == chat


@pytest.mark.parametrize(
    'status_code',
    [
        400, 401, 404, 500, 502
    ]
)
def test_telegram_api_service_raises_telegram_api_error(httpx_mock, telegram_api_service, status_code):
    httpx_mock.add_response(status_code=status_code)
    with pytest.raises(exceptions.TelegramAPIError) as error:
        telegram_api_service.get_chat(chat_id=1234)
    assert error.value.args[0] == 'Could not get chat from Telegram API'
