from dataclasses import dataclass
from typing import Self

__all__ = (
    'Chat',
    'TelegramChat',
)


@dataclass(frozen=True, slots=True)
class Chat:
    id: int
    type: str
    title: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None

    @property
    def full_name(self) -> str:
        """Get full name of the Chat.
        For private chat it is first_name + last_name.
        For other chat types it is title.
        """
        if self.title is not None:
            return self.title

        if self.last_name is not None:
            return f'{self.first_name} {self.last_name}'

        return f'{self.first_name}'

    @classmethod
    def from_response_data(cls, response_data: dict) -> Self:
        return cls(
            id=response_data['id'],
            type=response_data['type'],
            title=response_data.get('title'),
            username=response_data.get('username'),
            first_name=response_data.get('first_name'),
            last_name=response_data.get('last_name'),
        )


@dataclass(frozen=True, slots=True)
class TelegramChat:
    chat_id: int
    title: str | None = None

    @classmethod
    def from_response_data(cls, response_data: dict) -> Self:
        return cls(
            chat_id=response_data['chat_id'],
            title=response_data.get('title'),
        )
