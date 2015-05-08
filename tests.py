# -*- coding: utf-8 -*-
"""
    CoinMate.io unittests.
"""

import unittest
from coinmate_api import coinmate


class TestStringMethods(unittest.TestCase):
    """CoinMate.io unittests."""

    def setUp(self):
        self.cm = coinmate('privateApiKey', 'publicApiKey', '1111')
        self.cm.API_URL = 'https://private-anon-c924a24db-coinmate.apiary-mock.com/api/'

    def test_balance(self):
        balances = self.cm.get_balance()
        assert 'data' in balances
        assert 'USD' in balances['data']
        assert 'BTC' in balances['data']
        assert 'error' in balances

    def test_usd_balance(self):
        balances = self.cm.get_usd_balance()
        assert balances['currency'] == "USD"
        assert 'balance' in balances
        assert 'reserved' in balances
        assert 'available' in balances

    def test_btc_balance(self):
        balances = self.cm.get_btc_balance()
        assert balances['currency'] == "BTC"
        assert 'balance' in balances
        assert 'reserved' in balances
        assert 'available' in balances

    def test_usd_available(self):
        self.assertIs(type(self.cm.get_usd_available()), float)

    def test_btc_available(self):
        self.assertIs(type(self.cm.get_btc_available()), float)

if __name__ == '__main__':
    unittest.main()
