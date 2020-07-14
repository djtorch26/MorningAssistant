# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:30:45 2020

@author: Dawson
"""

from datetime import date
from pathlib import Path

"""
def NuggetType(nugget_type):
    
    if nugget == 'Email'
"""        

def openNuggetFile():
    txt = '.txt'
    Nuggie = "MorningNugget"
    Nugget = (Nuggie + timeNow() + txt)
    extender = ("../MorningNuggets/" + Nugget)
    
    base_path = Path(__file__).parent
    file_path = (base_path / extender).resolve()
    return file_path

def appendNuggetFile(text_data):
    f = open(openNuggetFile(), 'a')
    f.write(text_data)
    f.write('\n')
    f.close()

def timeNow():
    now = date.today()
    full = "_" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)
    return full

def replace_all(text,dic):
    for i, j in dic.iteritems():
        text = text.replace(i,j)
    return text