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
