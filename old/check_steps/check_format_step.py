from typing import Tuple
from copster.check_step import CheckStep
from sh import ruff

class CheckFormatStep(CheckStep):
    def get_name(self) -> str:
        return "format (ruff)"

    def pre(self) -> Tuple[bool, str]:
        if ruff(help=True).exit_code != 0:
            return False, "ruff not installed"

        return True, ""

    def run(self) -> bool:
        return True
