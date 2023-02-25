import pytest

import models


@pytest.mark.parametrize(
    'response_data, model',
    [
        (
                {
                    'id': 256617535672,
                    'first_name': 'Tim',
                    'last_name': 'Cook',
                    'username': None,
                    'type': 'private',
                },
                models.Chat(
                    id=256617535672,
                    first_name='Tim',
                    last_name='Cook',
                    username=None,
                    type='private',
                    title=None,
                ),
        ),
        (
                {
                    'id': -1001876075282,
                    'type': 'supergroup',
                    'title': 'Apple Team',
                    'username': None,
                    'first_name': None,
                    'last_name': None,
                },
                models.Chat(
                    id=-1001876075282,
                    first_name=None,
                    last_name=None,
                    username=None,
                    type='supergroup',
                    title='Apple Team',
                ),
        ),
    ]
)
def test_chat_from_response_data_constructor(response_data, model):
    assert models.Chat.from_response_data(response_data) == model


@pytest.mark.parametrize(
    'chat, full_name',
    [
        (
                models.Chat(
                    id=1234,
                    type='private',
                    first_name='Alex',
                ),
                'Alex',
        ),
        (
                models.Chat(
                    id=2345,
                    type='supergroup',
                    title='Friends',
                ),
                'Friends',
        ),
        (
                models.Chat(
                    id=3456,
                    type='private',
                    first_name='Benedict',
                    last_name='Cumberbatch',
                ),
                'Benedict Cumberbatch',
        ),
    ]
)
def test_chat_full_name_property(chat: models.Chat, full_name: str):
    assert chat.full_name == full_name
