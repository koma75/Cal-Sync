#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BSD 2-Clause License
# 
# Copyright (c) 2022 Yasuhiro Okuno <okunoya@path-works.net>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Main CLI Setup and Entrypoint."""

from __future__ import absolute_import, division, print_function

# Import the main click library
import click
# Import the sub-command implementations
from .calsync import calsync
# Import the version information
from cal_sync.version import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command()
@click.argument('ARG')
@click.option(
    '--flag', '-f', is_flag=True,
    help='some flag option'
    )
@click.option(
    '--config', '-c', default="./cal_sync.yml",
    type=click.Path(exists=False, dir_okay=False, writable=True, resolve_path=True),
    metavar='<cfg>',
    help='Configuration File (default: cal_sync.yml)'
    )
@click.option(
    '--fmt', '-f', default="defaultvalue", type=str,
    metavar='<fmt>',
    help='string option'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
@click.version_option(version=__version__)
def cli(**kwargs):
    """Outlook to Google Calendar sync CLI tool
    """
    calsync.cmd(kwargs)
    print(kwargs)
    pass

# Entry point
def main():
    """Main script."""
    cli()

if __name__ == '__main__':
    main()
