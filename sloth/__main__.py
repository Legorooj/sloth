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


@click.group(
    'sloth'
)
@click.version_option(__version__)
def cli():
    pass


@cli.command('speedtest-file')
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
    filename = file
    click.echo('Loading python file {}'.format(filename))
    with open(filename, 'rb') as file:
        test = TestExec(file.read())  # gbls and lcls are set to nothing; ie clean environment
        click.echo('Running file...')
        result = test.run()
        click.echo('{} took {} seconds to run'.format(filename, result))


if __name__ == '__main__':
    # cli()
    speedtest_file(['D:\\FluffyKoalas\\Sloth\\sloth.py'])