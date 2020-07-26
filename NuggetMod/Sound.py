# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 02:12:33 2020

@author: Dawson
"""

from gtts import gTTS
from . import FileManager as fmanager
#import playsound
import shutil
import pygame
import os


nuggetSpeech = fmanager.readNuggetFile()

def speak(text):
    tts = gTTS(text=text, lang = 'en')
#changes directory of file 
    try:
#creates and saves file from the daily .txt file
        saveFile = 'MorningNuggie'+ fmanager.timeNow() + '.mp3'
        tts.save(saveFile)
        #soundfile = open(save)
        #plays sound object for the daily .txt file that is generated.
        #playsound.playsound(saveFile)
        
        # pygame.mixer.init()
        # soundtoplay = pygame.mixer.music.load(os.path.join('/home/pi/Documents/MorningAssistant/', saveFile))
        # soundtoplay.play()
        # soundfile.close()
        #while pygame.mixer.music.get_busy() == True:
            #continue
        pathfrom = ('/home/pi/Documents/MorningAssistant/' + saveFile)
        pathto = '/home/pi/Documents/MorningAssistant/MorningNuggets/'
        shutil.move(pathfrom, pathto)
        
        os.system(pathto + saveFile)
    except Exception as e:
        print(e)
        
#speak(nuggetSpeech)



