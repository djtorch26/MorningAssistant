# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:50 2020

@author: Dawson
"""

import robin_stocks as r
import os
from . import FileManager as fmanager


r.login(str(os.getenv('GMAIL_USERNAME')), str(os.getenv('ROBINHOOD_PASSWORD')))


def getStockInfo():
    accountValue = str(r.profiles.load_portfolio_profile('extended_hours_market_value'))
    
    gluu = str(r.stocks.get_fundamentals('GLUU', 'open'))
    ual = str(r.stocks.get_fundamentals('UAL', 'open'))
    gpro = str(r.stocks.get_fundamentals('GPRO','open'))
    acb = str(r.stocks.get_fundamentals('ACB','open'))
    jets = str(r.stocks.get_fundamentals('JETS','open'))
    
    GLUU = parseOpenPrice(gluu)
    UAL = parseOpenPrice(ual)
    GPRO = parseOpenPrice(gpro)
    ACB = parseOpenPrice(acb)
    JETS = parseOpenPrice(jets)
    
    
    btc = str(r.crypto.get_crypto_quote('BTC', 'mark_price'))
    fBTC = float(btc)
    BTC = str(round(fBTC,2))
    
    doge = str(r.crypto.get_crypto_quote('DOGE', 'mark_price'))
    fdoge = float(doge)
    DOGE = str(round(fdoge,3))
    
    
    fAccount = float(accountValue)
    Account = str(round(fAccount,2))
    
    print(GLUU)
    print(UAL)
    print(GPRO)
    print(ACB)
    print(BTC)
    print(JETS)
    print(Account)
    
    #file_type = '.txt'
    #Name = 'MorningNugget'
    
    fmanager.openNuggetFile()
    fmanager.appendNuggetFile("Here is your Stock Portfolio Update," +
                             "\n" + f"Your Account's Total Value is {Account}," +
                             "\n" + f"Glue Mobile Market Price is {GLUU}," +
                             "\n" + f"United Airlines Market price is {UAL}," +
                             "\n" + f"Global JETS E T F Market price is {JETS}," +
                             "\n" + f"Go Pro Market Price is {GPRO}" +
                             "\n" + f"Aurora Cannabis Market price is {ACB}" +
                             "\n" +
                             "\n" + "Here is your Crypto Update," +
                             "\n" + f"Bit coin Market Price is {BTC}," +
                             "\n" + f"Doge coin Market Price is {DOGE}" +
                             "\n"
                              )

def parseOpenPrice(ticker):
    sub = ticker.replace('[', '')
    sub1 = sub.replace(']','')
    s = sub1.replace("'",'')
    fticker = float(s)
    roundedticker = str(round(fticker,2))
    return roundedticker
    
#getStockInfo()
