# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

import click
from sloth import __version__, compare_sloth
from sloth.raw.tests import TestExec
from importlib import import_module


CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group('sloth', context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(__version__)
def cli():
    """The sloth command line utility.
    Please type 'sloth [cmd] --help' for information about specific commands.
    """
    pass


@cli.command('speedtest-file', short_help='speedtest a file')
@click.argument(
    'file',
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True
    )
)
def speedtest_file(file):
    """Time the execution of FILE"""
    filename = file
    click.echo('Loading python file {}'.format(filename))
    with open(filename, 'rb') as file:
        test = TestExec(file.read())  # gbls and lcls are set to nothing; ie clean environment
        click.echo('Running file...')
        result = test.run()
        click.echo('{} took {!s} seconds to run'.format(filename, result))
        

@cli.command('compare', short_help='useless utility for showing off')
@click.argument('other', type=click.STRING)
def compare(other):
    """
    This command wraps the function sloth.compare_against(other)
    """
    try:
        mod = import_module(other)
        click.echo(compare_sloth(mod))
    except ModuleNotFoundError:
        click.echo(compare_sloth(other))
        


if __name__ == '__main__':
    # cli() - Removed to show error
    speedtest_file(['D:\\FluffyKoalas\\Sloth\\sloth.py'])