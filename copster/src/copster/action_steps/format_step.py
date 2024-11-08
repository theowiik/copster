from typing import Tuple

from sh import ruff

from copster.step import Step


class FormatStep(Step):
    def get_name(self) -> str:
        return "Format"

    def pre(self) -> Tuple[bool, str]:
        return self._simple_pre_check("ruff")

    def run(self) -> bool:
        ruff.format()
        ruff.check(select=["I"], fix=True)

        return True
