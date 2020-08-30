# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:30:48 2020

@author: Harry
"""

from abc import ABCMeta, abstractmethod
class Music():
    __metaclass__ = ABCMeta
    @abstractmethod
    def do_play(self):
        pass
class Mp3(Music):
    def do_play(self):
        print ("Playing .mp3 music!")

class Ogg(Music):
    def do_play(self):
        print ("Playing .ogg music!")

class MusicFactory(object):
    def play_sound(self, object_type):
        return eval(object_type)().do_play()

if __name__ == "__main__":
 mf = MusicFactory()
 music = input("Which music you want to play Mp3 or Ogg \n")
 mf.play_sound(music)