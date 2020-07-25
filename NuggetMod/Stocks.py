# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:12:50 2020

@author: Dawson
"""
from . import key as k
#import key as k
import robin_stocks as r
from . import stockHandler as sh
#import stockHandler as sh
import os


r.authentication.login(k.robinhoodAccount(), k.robinhoodPwrd(), expiresIn = 10, by_sms = True)

#ACCOUNT VALUE
accountValue = str(r.profiles.load_portfolio_profile('market_value'))
fAccount = float(accountValue)    
Account = str(round(fAccount,2))

stockListPath = 'C:\\Users\\bamba\\Documents\\Python_Scripts\\MorningAssistant\\NuggetMod\\stockList.txt'
stockfile = open(stockListPath, 'r')
stockContent = stockfile.read()
stockList = stockContent.split()
#print(stockList)
stockLister = stockContent.split(',')

#print(str(stockList[0]))

for i in stockList:
    stockPrice = sh.getNewStockPrice(i) 
    sh.addPrice(stockPrice)
    
priceLister = []

priceListPath = 'C:\\Users\\bamba\\Documents\\Python_Scripts\\MorningAssistant\\NuggetMod\\priceList.txt'
pricefile = open(priceListPath, 'r')
priceContent = pricefile.read()
priceLister = priceContent.split()

priceList = []

for j in priceLister:
    price = sh.parseOpenPrice(j)   
    priceList.append(price)
#print(priceList)

    
#CRYPTO CURRENCIES
btc = str(r.crypto.get_crypto_quote('BTC', 'mark_price'))
doge = str(r.crypto.get_crypto_quote('DOGE', 'mark_price'))

#PARSING CRYPTO FOR STRING VALUES
fBTC = float(btc)
BTC = str(round(fBTC,2))

fdoge = float(doge)
DOGE = str(round(fdoge,3))

r.authentication.logout()

def getStockInfo():
    sh.createStockReport(stockLister, priceList)
    
    path = 'C:\\Users\\bamba\\Documents\\Python_Scripts\\MorningAssistant\\NuggetMod\\stockBriefing.txt'
    report = open(path,'r')
    text = report.read()
    
    print(text)
    
    stockBriefing = ("Here is your Stock Portfolio Update," +
                     "\n" + f"Your Account's Total Value is {Account}," +
                     '\n' + text + '\n')
    
    print(stockBriefing)
    return stockBriefing

#getStockInfo()   

