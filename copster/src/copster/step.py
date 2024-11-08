from abc import ABC, abstractmethod
from typing import Tuple

import sh


class Step(ABC):
    def _simple_pre_check(self, cmd: str) -> Tuple[bool, str]:
        if sh.which(cmd) is not None:
            return True, ""

        return False, f"{cmd} is not installed"

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def pre(self) -> Tuple[bool, str]:
        pass

    @abstractmethod
    def run(self) -> bool:
        pass
