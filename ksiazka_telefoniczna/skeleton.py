#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
        hello_world = ksiazka_telefoniczna.module:function

Then run `python setup.py install` which will install the command `hello_world`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging

from ksiazka_telefoniczna import __version__

__author__ = "Dariusz Luczynski"
__copyright__ = "Dariusz Luczynski"
__license__ = "none"

_logger = logging.getLogger(__name__)


from ksiazka_telefoniczna.Console import Console

def run():
    '''
    Function run opens a console window with root menu of Książka Telefoniczna.
    '''
    c=Console()

if __name__ == "__main__":
    run()
