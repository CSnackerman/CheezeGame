from sys import exit

from pygame import quit
from pygame.event import get
from pygame.locals import *

from keyboard import Keyboard

class EventHandler:
    
    @staticmethod
    def pollEvents ():

        for e in get():

            if e.type == QUIT:
                print ("quitting...")
                quit()
                exit()

            Keyboard.handleEvents (e)

        Keyboard.handlePressed()