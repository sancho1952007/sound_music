from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

"""
Music Function
"""

from pygame import *
mixer.init()

def play(s):
   mixer.music.load(s)
   mixer.music.play()
   while mixer.music.get_busy():
    time.Clock().tick(0)

"""
Main File, Please Do Not Edit!
"""
