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
        self.cm.API_URL = 'https://private-anon-ef457d374-coinmate.apiary-mock.com/api/'

    def test_balance(self):
        balances = self.cm.get_balance()
        assert 'data' in balances
        assert 'EUR' in balances['data']
        assert 'BTC' in balances['data']
        assert 'error' in balances

    def test_eur_balance(self):
        balances = self.cm.get_eur_balance()
        assert balances['currency'] == "EUR"
        assert 'balance' in balances
        assert 'reserved' in balances
        assert 'available' in balances

    def test_btc_balance(self):
        balances = self.cm.get_btc_balance()
        assert balances['currency'] == "BTC"
        assert 'balance' in balances
        assert 'reserved' in balances
        assert 'available' in balances

    def test_eur_available(self):
        self.assertIs(type(self.cm.get_eur_available()), float)

    def test_btc_available(self):
        self.assertIs(type(self.cm.get_btc_available()), float)

    def test_withdraw_bitcoins(self):
        rs = self.cm.withdraw_bitcoins(2, '1HB1by2ZkbFAwEAqC5zwoHcU1DroBysrPG')
        assert not rs['error']
        self.assertIs(type(rs['data']), int)

    def test_get_ticker(self):
        ticker = self.cm.get_ticker()
        assert 'error' in ticker
        assert 'data' in ticker
        assert 'amount' in ticker['data']

    def test_get_ticker_low(self):
        ticker = self.cm.get_ticker_low()
        self.assertIs(type(ticker), int)

    def test_get_ticker_high(self):
        ticker = self.cm.get_ticker_high()
        self.assertIs(type(ticker), int)

    def test_get_ticker_last(self):
        ticker = self.cm.get_ticker_low()
        self.assertIs(type(ticker), int)

if __name__ == '__main__':
    unittest.main()
