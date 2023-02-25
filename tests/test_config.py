import os

import pytest

from config import load_config, Config


@pytest.mark.parametrize(
    'config_text, expected_config',
    [
        (
                '''[logging]
                level = "DEBUG"
                
                [database]
                url = "url"
                
                [telegram_bot]
                token = "token"''',
                Config(
                    logfile_path=None,
                    loglevel='DEBUG',
                    database_url='url',
                    telegram_bot_token='token',
                ),
        ),
        (
                '''[logging]
                level = "DEBUG"
                path = "/var/logs/log.log"
                
                [database]
                url = "url"
                
                [telegram_bot]
                token = "token"''',
                Config(
                    logfile_path='/var/logs/log.log',
                    loglevel='DEBUG',
                    database_url='url',
                    telegram_bot_token='token',
                ),
        ),
        (
                '''[logging]
                level = "DEBUG"
                path = ""
                
                [database]
                url = "url"
                
                [telegram_bot]
                token = "token"''',
                Config(
                    logfile_path=None,
                    loglevel='DEBUG',
                    database_url='url',
                    telegram_bot_token='token',
                ),
        ),
    ]
)
def test_config(config_text: str, expected_config: Config):
    with open('./temp_config.toml', 'w') as file:
        file.write(config_text)
    actual_config = load_config('./temp_config.toml')
    os.remove('./temp_config.toml')
    assert actual_config == expected_config
