from dataclasses import dataclass
from typing import Self

__all__ = ('Chat',)


@dataclass(frozen=True, slots=True)
class Chat:
    id: int
    type: str
    title: str | None
    username: str | None
    first_name: str | None
    last_name: str | None

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
