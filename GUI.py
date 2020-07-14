# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:25:38 2020

@author: Dawson
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:19:23 2020

@author: 
"""


# importing whole module 
from tkinter import * 
from tkinter.ttk import *
  
# importing strftime function to 
# retrieve system's time 
from time import strftime 
from datetime import datetime
import os
  
# creating tkinter window 
root = Tk() 
root.title('Clock') 
  
# This function is used to  
# display time on the label 
def time(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

def getTime():
    now = datetime.now()
    currentTime = now.strftime('%H:%M:%S')
    print(currentTime)
    return currentTime

def getSpotifyUser():
    Username = os.getenv('SPOTIFY_USERNAME')
    print(Username)
    return Username
    

# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('arial', 40, 'bold'), 
            background = 'Black', 
            foreground = 'white') 

btn = Button(root, text = 'Click here',
             command = getTime)
btn2 = Button(root, text = 'Spotify',
              command =  getSpotifyUser)
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
btn.pack(side = 'bottom')
btn2.pack(side = 'bottom')
time() 
  
mainloop() 
