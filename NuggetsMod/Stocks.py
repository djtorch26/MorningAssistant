# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:50 2020

@author: Dawson
"""

import robin_stocks as r
import os
import FileManager as fmanager


r.login(str(os.getenv('GMAIL_USERNAME')), str(os.getenv('ROBINHOOD_PASSWORD')))


def getStockInfo():
    accountValue = str(r.profiles.load_portfolio_profile('market_value'))
    Gluu = str(r.stocks.get_fundamentals('GLUU', 'open'))
    BTC = str(r.crypto.get_crypto_quote('BTC', 'mark_price'))
    
    subGluu = Gluu.replace('[', '')
    sub1Gluu = subGluu.replace(']','')
    sGluu = sub1Gluu.replace("'",'')
    
    print(sGluu)
    print(BTC)
    print(accountValue)
    
    fmanager.openNuggetFile()
    fmanager.appendNuggetFile(f"Gluu Market Price: {sGluu}")
    fmanager.appendNuggetFile(f"BTC Market Price: {BTC}")
    fmanager.appendNuggetFile(f"Account Total Value: {accountValue}")
    
#getStockInfo()