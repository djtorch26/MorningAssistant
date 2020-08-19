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



def getSpotifyUser():
    Username = os.getenv('SPOTIFY_USERNAME')
    print(Username)
    return 

# This function is used to  
# display time on the label 
def time(lbl): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(1000, time)
    
def getTime():
    now = datetime.now()
    currentTime = now.strftime('%H:%M:%S')
    print(currentTime)
    return currentTime


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        
        quitButton = Button(self, text="Exit",command=self.client_exit)
        quitButton.place(x=0, y=0)
        
        
        

        lbl = Label(self, font = ('arial', 40, 'bold'),
                        background = 'Black', 
                        foreground = 'white')    
        lbl.pack(anchor = 'center')
        time(lbl = lbl)
        
        def client_exit(self): 
            exit()
        



      
        
# creating tkinter window 
root = Tk() 

root.geometry("480x360")
app = Window(root)
 
root.mainloop() 




# # Styling the label widget so that clock 
        # # will look more attractive 
        # lbl = Label(root, font = ('arial', 40, 'bold'), 
        #     background = 'Black', 
        #     foreground = 'white') 

        # btn = Button(root, text = 'Click here',
        #      command = getTime)
        # btn2 = Button(root, text = 'Spotify',
        #       command =  getSpotifyUser)
        # # Placing clock at the centre 
        # # of the tkinter window 
        # lbl.pack(anchor = 'center') 
        # btn.pack(side = 'bottom')
        # btn2.pack(side = 'bottom')
        # time()