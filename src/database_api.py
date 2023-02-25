import contextlib

import httpx

import models

__all__ = (
    'closing_database_api_client',
    'DatabaseAPIService',
)


@contextlib.contextmanager
def closing_database_api_client(*, base_url: str) -> httpx.Client:
    with httpx.Client(base_url=base_url) as client:
        yield client


class DatabaseAPIService:

    def __init__(self, *, api_client: httpx.Client):
        self.__api_client = api_client

    def get_telegram_chats(self) -> list[models.TelegramChat]:
        is_end_of_list_reached = False
        url = '/telegram-chats/'
        telegram_chats = []
        limit: int = 100
        offset: int = 0
        while not is_end_of_list_reached:
            request_query_params = {'limit': limit, 'offset': offset}
            response = self.__api_client.get(url, params=request_query_params)
            response_data = response.json()
            is_end_of_list_reached = response_data['is_end_of_list_reached']
            telegram_chats += response_data['telegram_chats']
            offset += limit
        return [models.TelegramChat.from_response_data(telegram_chat) for telegram_chat in telegram_chats]

    def update_telegram_chat(self, *, chat_id: int, title: str | None):
        url = f'/telegram-chats/{chat_id}/'
        request_data = {'title': title}
        response = self.__api_client.put(url, json=request_data)
        if response.is_error:
            raise
