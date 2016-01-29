#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for ksiazka_telefoniczna.

    This file was generated with PyScaffold 2.5.3, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup,find_packages


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
            # use_pyscaffold=True,)
            use_pyscaffold=True,
            package_dir = {'ksiazka_telefoniczna': 'ksiazka_telefoniczna'},
            include_package_data = True,
            packages=find_packages(),

            #NOK
            # package_data = [('cfg', ['cfg/*.json']),
            #     ('db', ['db/*.db']),
            #     ('csv', ['csv/*.csv'])])
            # data_files = {
            # package_data = {
            # of the 'mypkg' package, also:
            #     'cfg': ['ksiazka_telefoniczna/cfg/*.json'],'db':['ksiazka_telefoniczna/db/*.db'],'csv':['ksiazka_telefoniczna/csv/*.csv']})
            # 'ksiazka_telefoniczna': ['cfg/*.json','db/*.db','csv/*.csv']})

            #ok
            # data_files = ['/cfg/*.json'])
            # data_files = {'cfg': ['/cfg/*.json'],'db':['/db/*.db'],'csv':['/csv/*.csv']})
            # package_data = {'cfg': ['/cfg/*.json'],'db':['/db/*.db'],'csv':['/csv/*.csv']})
            #
            #nok
            # data_files = ['.ksiazka_telefoniczna/cfg'])
            #ok
            package_data = {'': ['cfg/*.json',
                                'db/*.db',
                                'csv/*.csv']})


if __name__ == "__main__":
    setup_package()
