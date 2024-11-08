from typing import Tuple

from copster.step import Step


class MyPyCheck(Step):
    def get_name(self) -> str:
        pass

    def pre(self) -> Tuple[bool, str]:
        return self._simple_pre_check("mypy")

    def run(self) -> bool:
        return True
