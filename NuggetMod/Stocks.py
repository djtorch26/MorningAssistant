# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:50 2020

@author: Dawson
"""

import robin_stocks as r
import os
import FileManager as fmanager ####ADD 'from .'


r.login(str(os.getenv('GMAIL_USERNAME')), str(os.getenv('ROBINHOOD_PASSWORD')))

def getStockInfo():
    
    
    
    accountValue = str(r.profiles.load_portfolio_profile('market_value'))
    
    gluu = str(r.stocks.get_quotes('GLUU', 'ask_price'))
    ual = str(r.stocks.get_quotes('UAL', 'ask_price'))
    gpro = str(r.stocks.get_quotes('GPRO','ask_price'))
    acb = str(r.stocks.get_quotes('ACB','ask_price'))
    jets = str(r.stocks.get_quotes('JETS','ask_price'))
    
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
    

    
    stockBriefing = ("Here is your Stock Portfolio Update," +
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
    
    r.authentication.logout()
    
    return stockBriefing

def parseOpenPrice(ticker):
    sub = ticker.replace('[', '')
    sub1 = sub.replace(']','')
    s = sub1.replace("'",'')
    fticker = float(s)
    roundedticker = str(round(fticker,2))
    return roundedticker


def test():
    #accountValue = str(r.profiles.load_portfolio_profile('market_value'))
    #print(accountValue)
    print(float(r.profiles.load_portfolio_profile('market_value'))+7.45)
    r.authentication.logout()
    #print(getStockInfo())
    

test()
    
#getStockInfo()
    
    #file_type = '.txt'
    #Name = 'MorningNugget'
    
    #fmanager.openNuggetFile()

'''
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
'''