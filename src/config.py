import pathlib
import tomllib
from dataclasses import dataclass

__all__ = (
    'Config',
    'load_config',
)


@dataclass(frozen=True, slots=True)
class Config:
    logfile_path: str | None
    loglevel: str
    telegram_bot_token: str
    database_url: str


def load_config(logfile_path: str | pathlib.Path) -> Config:
    with open(logfile_path, 'rb') as file:
        config = tomllib.load(file)

    return Config(
        logfile_path=config['logging'].get('path'),
        loglevel=config['logging']['level'],
        database_url=config['database']['url'],
        telegram_bot_token=config['telegram_bot']['token'],
    )
