import pathlib

import telegram
from config import load_config
from database_api import closing_database_api_client, DatabaseAPIService


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.toml'
    config = load_config(config_file_path)

    with closing_database_api_client(base_url=config.database_url) as database_api_client:

        with telegram.closing_telegram_api_client(bot_token=config.telegram_bot_token) as telegram_api_client:

            telegram_api_service = telegram.TelegramAPIService(api_client=telegram_api_client)
            database_api_service = DatabaseAPIService(api_client=database_api_client)

            telegram_chats = database_api_service.get_telegram_chats()
            for telegram_chat in telegram_chats:
                chat = telegram_api_service.get_chat(chat_id=telegram_chat.chat_id)

                if chat.full_name == telegram_chat.title:
                    continue

                database_api_service.update_telegram_chat(chat_id=chat.id, title=chat.full_name)


if __name__ == '__main__':
    main()
