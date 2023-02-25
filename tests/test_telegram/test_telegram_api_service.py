import pytest

import exceptions
import models
from telegram import TelegramAPIService


class FakeSuccessfulResponse:
    status_code = 200

    def __init__(self, response_data: dict):
        self.__response_data = response_data

    def json(self) -> dict:
        return {'result': self.__response_data}


class FakeResponseWithCustomStatusCode:

    def __init__(self, status_code: int):
        self.status_code = status_code


class FakeTelegramAPIClient:

    def __init__(self, response):
        self.__response = response

    def get(self, *args, **kwargs):
        return self.__response


@pytest.mark.parametrize(
    'telegram_api_client, chat',
    [
        (
                FakeTelegramAPIClient(FakeSuccessfulResponse({
                    'id': 1234,
                    'type': 'private',
                    'first_name': 'Alex',
                })),
                models.Chat(
                    id=1234,
                    type='private',
                    first_name='Alex',
                ),
        ),
        (
                FakeTelegramAPIClient(FakeSuccessfulResponse({
                    'id': 1234,
                    'type': 'supergroup',
                    'title': 'Managers',
                    'username': 'managers',
                })),
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


@pytest.mark.parametrize(
    'telegram_api_client',
    [
        FakeTelegramAPIClient(FakeResponseWithCustomStatusCode(400)),
        FakeTelegramAPIClient(FakeResponseWithCustomStatusCode(401)),
        FakeTelegramAPIClient(FakeResponseWithCustomStatusCode(404)),
        FakeTelegramAPIClient(FakeResponseWithCustomStatusCode(500)),
        FakeTelegramAPIClient(FakeResponseWithCustomStatusCode(502)),
    ]
)
def test_telegram_api_service_raises_telegram_api_error(telegram_api_client):
    with pytest.raises(exceptions.TelegramAPIError) as error:
        assert TelegramAPIService(api_client=telegram_api_client).get_chat(chat_id=1234)
    assert error.value.args[0] == 'Could not get chat from Telegram API'
