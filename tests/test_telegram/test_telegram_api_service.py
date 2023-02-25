import pytest

import models
from telegram import TelegramAPIService


class FakeResponse:

    def __init__(self, response_data: dict):
        self.__response_data = response_data

    def json(self) -> dict:
        return {'result': self.__response_data}


class FakeTelegramAPIClient:

    def __init__(self, response_data: dict):
        self.__response_data = response_data

    def get(self, *args, **kwargs) -> FakeResponse:
        return FakeResponse(self.__response_data)


@pytest.mark.parametrize(
    'telegram_api_client, chat',
    [
        (
                FakeTelegramAPIClient({
                    'id': 1234,
                    'type': 'private',
                    'first_name': 'Alex',
                }),
                models.Chat(
                    id=1234,
                    type='private',
                    first_name='Alex',
                ),
        ),
        (
                FakeTelegramAPIClient({
                    'id': 1234,
                    'type': 'supergroup',
                    'title': 'Managers',
                    'username': 'managers',
                }),
                models.Chat(
                    id=1234,
                    type='supergroup',
                    title='Managers',
                    username='managers',
                ),
        ),
    ]
)
def test_telegram_api_service_get_chats(telegram_api_client, chat):
    assert TelegramAPIService(api_client=telegram_api_client).get_chat(chat_id=1234) == chat
