from typing import List

import click

from copster.__about__ import __version__
from copster.cli.check_step import CheckStep
from copster.cli.check_steps.check_format_step import CheckFormatStep


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="copster")
def copster():
    click.echo("Hello world!")
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
