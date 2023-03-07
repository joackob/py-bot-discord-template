from abc import abstractmethod
from dataclasses import dataclass
from collections.abc import Callable, Awaitable


class IAChat:
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def chat(self, query: str) -> str:
        raise NotImplementedError


@dataclass
class Bot:
    _event_chat: Callable[[None], Awaitable[None]] = None

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @property
    def event_chat(self):
        return self._event_chat

    @event_chat.setter
    def event_chat(self, handle: Callable):
        self._event_chat = handle

    @abstractmethod
    async def get_query(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def send_response(self, response: str) -> None:
        raise NotImplementedError
