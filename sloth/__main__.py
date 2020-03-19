# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

import click
from sloth import __version__, compare_sloth
from sloth.raw.tests import TestExec
from sloth.raw.runners import TestRunner
from importlib import import_module
from decimal import Decimal


CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group('sloth', context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(__version__)
def cli():
    """The sloth command line utility.
    Please type 'sloth [cmd] --help' for information about specific commands.
    """


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
        

@cli.command('speedtest-snippet', short_help='speedtest a code snippet')
@click.argument('snippet', type=click.STRING)
@click.option('-a', '--average', default=1, type=click.INT, help='Number of times to execute SNIPPET')
@click.option('-p', '--pre', default=10, type=click.INT,
              help='Controls the truncation of the results, in decimal places. Use -1 for no truncation. Defaults to 10'
              )
def speedtest_snippet(snippet, average, pre):
    """
    Speedtest a snippet of code
    """
    if pre == 0:
        click.echo('Invalid value 0 for precision argument')
    if average > 1:
        values = []
        with click.progressbar(length=average) as bar:
            test = TestRunner([TestExec(snippet)]*average)
            for i in test.run():
                values.append(i)
                bar.update(1)
        result = sum(values) / average
        mini = min(values)
        maxi = max(values)
        click.echo(
            '{} executions:\n'
            'fastest: {mini}s\n'
            'slowest: {maxi}s\n'
            'average: {re}s'.format(
                average,
                mini=str(Decimal(mini))[:pre],
                maxi=str(Decimal(maxi))[:pre],
                re=str(Decimal(result))[:pre]
            )
        )
    else:
        test = TestExec(snippet)
        click.echo('Starting test')
        click.echo('Loading snippet')
        click.echo('1 execution took {} seconds.'.format(Decimal(test.run())))


if __name__ == '__main__':
    cli()
