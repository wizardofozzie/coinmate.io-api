# -*- coding: utf-8 -*-
"""
 CoinMate.io API implementation.
"""

from urllib2 import Request, urlopen
from urllib import urlencode
import hmac
import hashlib
import time
import json


class coinmate:
    """ Main API class."""
    API_URL = "https://coinmate.io/api/"

    def __init__(self, privateApiKey, publicApiKey, clientId, nonce=None):
        """ API base contructor."""
        self.privateApiKey = str(privateApiKey)
        self.publicApiKey = str(publicApiKey)
        self.clientId = str(clientId)
        if not nonce:
            self.nonce = lambda: str(int(time.time()))

    def create_signature(self, nonce):
        """ This functions generate the signature."""
        signature = nonce + self.clientId + self.publicApiKey
        dig = hmac.new(
            self.privateApiKey,
            msg=signature,
            digestmod=hashlib.sha256
        ).hexdigest()
        signature = dig.encode('utf-8')
        return signature.upper()

    def get_balance(self):
        """ Get account balance."""
        nonce = self.nonce()
        values = urlencode({
            'clientId': self.clientId,
            'nonce': nonce,
            'signature': self.create_signature(nonce)
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        request = Request(
            self.API_URL+'balances',
            data=values,
            headers=headers
        )
        response_body = urlopen(request).read()
        return json.loads(response_body)

    def get_usd_balance(self):
        """ Get account USD balance."""
        balance = self.get_balance()
        if balance['error']:
            return None
        else:
            return balance['data']['USD']

    def get_usd_available(self):
        """ Get account USD balance available."""
        balance = self.get_balance()
        if balance['error']:
            return None
        else:
            return round(float(balance['data']['USD']['available']), 2)

    def get_btc_balance(self):
        """ Get account BitCoins balance."""
        balance = self.get_balance()
        if balance['error']:
            return None
        else:
            return balance['data']['BTC']

    def get_btc_available(self):
        """ Get account BitCoins balance available."""
        balance = self.get_balance()
        if balance['error']:
            return None
        else:
            return round(float(balance['data']['BTC']['available']), 8)
