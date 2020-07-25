# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:01:17 2020

Main Program file, run this file to open the alarm clock gui and begin your daily routine

@author: Dawson
"""

from __future__ import absolute_import
#from NuggetMod import EmailScreener as email
from NuggetMod import News as news
from NuggetMod import Stocks as stocks
from NuggetMod import Weather as weather
from NuggetMod import FileManager as fmanager
from NuggetMod import GoodMorning as gm
from NuggetMod import Sound as sound
from NuggetMod import key
import os

def main():
    
    CompleteNugget = (gm.goodMorning() + '\n' +
                  weather.getWeather() + '\n' +
                  stocks.getStockInfo() + '\n')
    testNug = ('Testing Complete')
    
    fmanager.writeNuggetFile(CompleteNugget)
    
    todaysNugget = fmanager.readNuggetFile()
    sound.speak(todaysNugget)
    
    
    
if __name__ == '__main__':
    main()