# SPDX-FileCopyrightText: 2024-present theowiik <theo.le.wiik@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from copster.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="copster")
def copster():
    click.echo("Hello world!")
