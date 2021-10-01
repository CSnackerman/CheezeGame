from sys import exit

from pygame import quit
from pygame.event import get, post, Event
from pygame.locals import *

from keyboard import Keyboard
from mouse import Mouse

class EventHandler:
    
    @staticmethod
    def pollEvents ():

        for e in get():

            if e.type == QUIT:
                print ("quitting...")
                quit()
                exit()

            Keyboard.handleEvents (e)
            Mouse.handleEvents(e)

        Keyboard.handlePressed()

    @staticmethod
    def postQuit ():
        post (Event(QUIT))
