import pytest

from telegram import closing_telegram_api_client


@pytest.mark.parametrize('bot_token', ['mysecrettoken', '123456', 'token'])
def test_telegram_api_client_creation_with_token(bot_token: str):
    with closing_telegram_api_client(bot_token=bot_token) as client:
        assert client.base_url == f'https://api.telegram.org/bot{bot_token}/'


@pytest.mark.parametrize('bot_token', ['', None])
def test_telegram_api_client_creation_without_token(bot_token):
    with pytest.raises(ValueError) as error:
        with closing_telegram_api_client(bot_token=bot_token):
            pass
    assert error.value.args[0] == 'Provide bot token in Telegram API client factory'
