from abc import abstractmethod


class IAChat:
    @abstractmethod
    def chat(self, message: str) -> str:
        raise NotImplementedError


class Bot:
    @abstractmethod
    def chatWith(self, ia: IAChat) -> None:
        raise NotImplementedError
