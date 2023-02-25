import contextlib

import httpx

import models

__all__ = (
    'closing_telegram_api_client',
    'TelegramAPIService',
)


@contextlib.contextmanager
def closing_telegram_api_client(*, bot_token: str) -> httpx.Client:
    if not bot_token:
        raise ValueError('Provide bot token in Telegram API client factory')

    base_url = f'https://api.telegram.org/bot{bot_token}/'
    with httpx.Client(base_url=base_url) as client:
        yield client


class TelegramAPIService:

    def __init__(self, api_client: httpx.Client):
        self.__api_client = api_client

    def get_chat(self, *, chat_id: int) -> models.Chat:
        url = '/getChat'
        request_query_params = {'chat_id': chat_id}
        response = self.__api_client.get(url, params=request_query_params)
        response_data = response.json()
        return models.Chat.from_response_data(response_data['result'])
