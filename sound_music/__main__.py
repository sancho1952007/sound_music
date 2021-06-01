from sound_music import *
import os
print("Use the play() method to play music using sound_music\nFor more info visit: https://sites.google.com/view/soundmusic")
print("\nGo to the directory where you have music files and run 'python -m sound_music' This will play the songs automatically in the directory!")
for music in os.listdir():
    if music.endswith(".mp3"):
       print("\nplaying '"+music+"' using 'sound_music' module in python")
       play(music)
    else:
        None

"""
Simple Test of the module...
"""
