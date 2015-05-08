# -*- coding: utf-8 -*-
"""
    Setup for CoinMate.io API wrapper.
"""

from distutils.core import setup

setup(
    name = 'coinmate-api',
    keywords = ['bitcoin', 'coinmate.io', 'bitcoin api'],
    url = 'https://github.com/tty02-fl/coinmate.io-api',
    requires = 'hashlib',
    install_requires = ['hashlib'],
    packages = ['coinmate_api'],
    package_dir = {'': 'src'},
    version = '0.0.1',
    description = 'CoinMate.io BitCoin processor API.',
    author = 'tty02-fl on github',
    author_email = 'tty02.fl@gmail.com',
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development'],
    long_description = '''
Coinmate.io API wrapper
-----------------------

Basic CoinMate.io API wrapper, for now it only support get the balance ::

    from coinmate_api import coinmate
    cm_api = coinmate('privateApiKey', 'publicApiKey', '3333')
    cm_api.get_usd_available()
''')
