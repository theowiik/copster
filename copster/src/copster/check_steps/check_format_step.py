from typing import Tuple

from sh import ErrorReturnCode, ruff

from copster.step import Step


class CheckFormatStep(Step):
    def get_name(self) -> str:
        return "Check formatting"

    def pre(self) -> Tuple[bool, str]:
        return self._simple_pre_check("ruff")

    def run(self) -> bool:
        try:
            ruff.format(check=True)
            ruff.check(select=["I"])

        except ErrorReturnCode:
            return False

        return True
