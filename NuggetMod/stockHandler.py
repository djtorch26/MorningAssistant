# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:59:15 2020

@author: Dawson
"""

import robin_stocks as r

def getNewStockPrice(stockName):
    newStock = str(r.stocks.get_quotes(stockName, 'ask_price'))
    return newStock

def setStockString(name, price):
    words = (f"{name} Market Price is {price}," + '\n')
    return words

def parseOpenPrice(ticker):
    sub = ticker.replace('[', '')
    sub1 = sub.replace(']','')
    sub2 = sub1.replace(',','')
    s = sub2.replace("'",'')
    fticker = float(s)
    roundedticker = str(round(fticker,2))
    return roundedticker

def addStock(stockTicker):
    newStock = (',' + stockTicker)
    path = 'C:\\Users\\bamba\\Documents\\Python_Scripts\\MorningAssistant\\NuggetMod\\stockList.txt'
    f = open(path, 'a')
    f.write(newStock)
    f.close()

def addPrice(price):
    newPrice = (price)
    path = 'C:\\Users\\bamba\\Documents\\Python_Scripts\\MorningAssistant\\NuggetMod\\priceList.txt'
    f = open(path, 'w')
    f.write(newPrice)
    
#testing variables
#Stocks = ['acb','ual','hammer']
#Prices = ['9.2','3.4','5.4']

def createStockReport(Stocks, Prices): 
    
    f = open('stockBriefing.txt', 'w')
    
    listDict = dict(zip(Stocks, Prices))
    print(listDict)
    
    for i in listDict:  
        f.writelines(setStockString(i, listDict[i]))
    f.close()  
    
#createStockReport(Stocks, Prices)
    

            
            
            
            
            