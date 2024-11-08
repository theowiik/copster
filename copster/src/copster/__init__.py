from argparse import ArgumentParser, Namespace
from typing import Dict, List

from copster.action_steps.format_step import FormatStep
from copster.check_steps.check_format_step import CheckFormatStep
from copster.check_steps.mymy_check import MyPyCheck
from copster.emoji import fail, pass_, print_logo
from copster.step import Step


def _parse_args() -> Namespace:
    args = ArgumentParser()
    args.add_argument("action", choices=["format", "check"])
    return args.parse_args()


def main() -> None:
    print_logo()

    args = _parse_args()
    if args.action == "format":
        _run_actions()

    if args.action == "check":
        _run_checks()


def _run_actions() -> None:
    actions: List[Step] = [FormatStep()]
    _run_steps(actions)


def _run_checks() -> None:
    checks: List[Step] = [CheckFormatStep(), MyPyCheck()]
    _run_steps(checks)


class StepState:
    success: bool = False
    msg: str = ""

    def __init__(self, step: Step):
        self.step = step


def _run_steps(steps: List[Step]) -> None:
    states: List[StepState] = [StepState(step) for step in steps]

    for state in states:
        step: Step = state.step
        pre_check_ok, msg = step.pre()

        if not pre_check_ok:
            print(f"{fail} {msg}")
            state.msg = f"Precheck failed: {msg}"
            continue

        res = step.run()

        if res:
            print(f"{pass_} {step.get_name()}")
            state.success = True
        else:
            print(f"{fail} {step.get_name()}")
            state.msg = f"Step failed: {step.get_name()}"

    for state in states:
        print(state.msg)
