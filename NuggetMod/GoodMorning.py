# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:27:24 2020

@author: Dawson
"""

from datetime import date
from . import key

dayNames = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
    }

monthNames = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
    }

numberNames = {
    1:'First',
    2:'Second',
    3:'Third',
    4:'Fourth',
    5:'Fifth',
    6:'Sixth',
    7:'Seventh',
    8:'Eighth',
    9:'Ninth',
    10:'Tenth',
    11:'Eleventh',
    12:'Twelth',
    13:'Thirteenth',
    14:'Fourteenth',
    15:'Fifteenth',
    16:'Sixteenth',
    17:'Seventeenth',
    18:'Eighteenth',
    19:'Nineteenth',
    20:'Twentieth',
    21:'Twenty First',
    22:'Twenty Second',
    23:'Twenty Third',
    24:'Twenty Fourth',
    25:'Twenty Fifth',
    26:'Twenty Sixth',
    27:'Twenty Seventh',
    28:'Twenty Eighth',
    29:'Twenty Ninth',
    30:'Thirtieth',
    31:'Thirty First'
    }
lorde = 'trogdor' #our one and only savior from the oldentimes. haha line 69 

def goodMorning():
    dayName = date.today().weekday()
    now = date.today()
    
    day = dayNames[dayName]
    dayNumber = numberNames[now.day]
    month = monthNames[now.month]
    year = str(now.year)
    YOURNAME = key.getName()
    
    OpeningBrief = f"Good Morning {YOURNAME}, Today is {day}, the {dayNumber} of {month}, in the year of our lorde {year}"
    
    print(OpeningBrief)
    print('opening brief complete')
    #fmanager.openNuggetFile()
    #fmanager.appendNuggetFile(OpeningBrief)
    return OpeningBrief

goodMorning()
