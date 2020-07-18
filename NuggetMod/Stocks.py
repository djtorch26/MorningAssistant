# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:50 2020

@author: Dawson
"""

import robin_stocks as r
import os
from . import FileManager as fmanager ####ADD 'from .'


r.login(str(os.getenv('GMAIL_USERNAME')), str(os.getenv('ROBINHOOD_PASSWORD')))

#ACCOUNT VALUE
accountValue = str(r.profiles.load_portfolio_profile('market_value'))
fAccount = float(accountValue)    
Account = str(round(fAccount,2))

#STOCKS
gluu = str(r.stocks.get_quotes('GLUU', 'ask_price'))
ual = str(r.stocks.get_quotes('UAL', 'ask_price'))
gpro = str(r.stocks.get_quotes('GPRO','ask_price'))
acb = str(r.stocks.get_quotes('ACB','ask_price'))
jets = str(r.stocks.get_quotes('JETS','ask_price'))
dis = str(r.stocks.get_quotes('DIS', 'ask_price'))


def setStockString(name, stockticker):
    words = f"{name} Market Price is {stockticker},"
    return words

def parseOpenPrice(ticker):
    sub = ticker.replace('[', '')
    sub1 = sub.replace(']','')
    s = sub1.replace("'",'')
    fticker = float(s)
    roundedticker = str(round(fticker,2))
    return roundedticker

#PARSING STOCKS FOR STRING VALUES
GLUU = parseOpenPrice(gluu)
UAL = parseOpenPrice(ual)
GPRO = parseOpenPrice(gpro)
ACB = parseOpenPrice(acb)
JETS = parseOpenPrice(jets)
DIS = parseOpenPrice(dis)

#CRYPTO CURRENCIES
btc = str(r.crypto.get_crypto_quote('BTC', 'mark_price'))
doge = str(r.crypto.get_crypto_quote('DOGE', 'mark_price'))

#PARSING CRYPTO FOR STRING VALUES
fBTC = float(btc)
BTC = str(round(fBTC,2))

fdoge = float(doge)
DOGE = str(round(fdoge,3))


def getStockInfo():
    stockBriefing = ("Here is your Stock Portfolio Update," +
                     "\n" + f"Your Account's Total Value is {Account}," +
                     "\n" + setStockString('Glu Mobile', GLUU) +
                     "\n" + setStockString('United Airlines', UAL) +
                     "\n" + setStockString('Global Jets E T F', JETS) +
                     "\n" + setStockString("Disney", DIS) +
                     "\n" + setStockString('Go Pro', GPRO) +
                     "\n" + setStockString('Aurora Cannibis', ACB) +
                     "\n" +
                     "\n" + "Here is your Crypto Update," +
                     "\n" + setStockString('Bit Coin', BTC) +
                     "\n" + setStockString('Doge Coin', DOGE) +
                     "\n"
                     )
    r.authentication.logout()
    print(stockBriefing)
    return stockBriefing
getStockInfo()
    

