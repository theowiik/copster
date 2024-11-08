from typing import List

from copster.check_step import CheckStep
from copster.check_steps.check_format_step import CheckFormatStep


def main() -> None:
    print("Hello from copster!")
    _demo_test()


def _demo_test():
    checks: List[CheckStep] = [CheckFormatStep()]

    for check in checks:
        print("Running check", check.get_name())
        res, msg = check.pre()

        if not res:
            print(msg)
            return

        res = check.run()
