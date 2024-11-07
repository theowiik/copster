from typing import List
from .check_steps.check_format_step import CheckFormatStep
from .check_step import CheckStep


def _run() -> None:
    checks: List[CheckStep] = [CheckFormatStep()]

    for check in checks:
        print("Running check", check.get_name())
        res, msg = check.pre()

        if not res:
            print(msg)
            return
        
        res = check.run()

if __name__ == "__main__":
    _run()
