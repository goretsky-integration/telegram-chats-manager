import contextlib

import httpx

__all__ = ('closing_telegram_api_client',)


@contextlib.contextmanager
def closing_telegram_api_client(*, bot_token: str) -> httpx.Client:
    if not bot_token:
        raise ValueError('Provide bot token in Telegram API client factory')

    base_url = f'https://api.telegram.org/bot{bot_token}/'
    with httpx.Client(base_url=base_url) as client:
        yield client
