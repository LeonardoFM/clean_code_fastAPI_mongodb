from abc import ABC, abstractmethod
from typing import Generic, TypeVar


Params = TypeVar('Params')
Return = TypeVar('Return')


class UseCase(ABC, Generic[Params, Return]):

    @abstractmethod
    def execute(self, params: Params) -> Return:
        raise NotImplementedError()
