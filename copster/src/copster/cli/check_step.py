from abc import ABC, abstractmethod
from typing import Tuple


class CheckStep(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def pre(self) -> Tuple[bool, str]:
        pass

    @abstractmethod
    def run(self) -> bool:
        pass
