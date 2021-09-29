from pygame.key import get_pressed
from pygame.locals import *
from pygame.event import post, Event


class Keyboard:

    @staticmethod
    def handlePressed():
        pressed = get_pressed()
        if pressed [K_RETURN]:
            print ('RETURN pressed')


    @staticmethod
    def handleEvents(e):
        if e.type == KEYDOWN:
            Keyboard.handleKeyDowns (e)
        if e.type == KEYUP:
            Keyboard.handleKeyUps (e)



    # utility functions

    @staticmethod
    def handleKeyDowns(e):
        if e.key == K_7:
            print ('7 DOWN')
            return
        if e.key == K_ESCAPE:
            post (Event (QUIT))
            return


    @staticmethod
    def handleKeyUps (e):
        if e.key == K_7:
            print ('7 UP')
            return
