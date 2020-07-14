# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:50 2020

@author: Dawson
"""

import robin_stocks as r
import os

r.login(str(os.getenv('GMAIL_USERNAME')), str(os.getenv('ROBINHOOD_PASSWORD')))


def getStockInfo():
    accountValue = r.profiles.load_portfolio_profile()
    Gluu = r.stocks.get_fundamentals('GLUU', 'open')
    BTC = r.crypto.get_crypto_quote('BTC', 'mark_price')
    print(Gluu)
    print(BTC)
    print(accountValue)
    
getStockInfo()