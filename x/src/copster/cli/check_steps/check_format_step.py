from typing import Tuple

from sh import ruff

from copster.cli.check_step import CheckStep


class CheckFormatStep(CheckStep):
    def get_name(self) -> str:
        return "format (ruff)"

    def pre(self) -> Tuple[bool, str]:
        if ruff(help=True).exit_code != 0:
            return False, "ruff not installed"

        return True, ""

    def run(self) -> bool:
        return True
