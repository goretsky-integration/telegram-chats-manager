import pytest

import models


@pytest.mark.parametrize(
    'response_data, model',
    [
        (
                {
                    'chat_id': 1234,
                    'title': 'Managers',
                },
                models.TelegramChat(chat_id=1234, title='Managers'),
        ),
        (
                {
                    'chat_id': 2345,
                    'title': None,
                },
                models.TelegramChat(chat_id=2345),
        ),
        (
                {
                    'chat_id': 3456,
                },
                models.TelegramChat(chat_id=3456),

        ),
    ]
)
def test_telegram_chat_from_response_data_constructor(response_data, model):
    assert models.TelegramChat.from_response_data(response_data) == model
