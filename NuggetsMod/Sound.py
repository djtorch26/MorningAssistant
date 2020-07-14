# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 02:12:33 2020

@author: Dawson
"""


import os
import spotify

config = spotify.Config()
config.user_agent = 'My awesome Spotify client'
config.tracefile = b'/tmp/libspotify-trace.log'

session = spotify.Session(config)

audio = spotify.AlsaSink(session)
loop = spotify.EventLoop(session)
loop.start()


session.login('djtorch123@gmail.com', 'YphbDush123#')

track = session.get_track('spotify:show:5RllMBgvDnTau8nnsCUdse')
track.load()
session.player.load(track)
session.player.play()