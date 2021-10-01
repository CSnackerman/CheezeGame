from pygame import Vector2
from pygame.locals import *
import pygame.event
import pygame.mouse

class Mouse:

    observers = []

    @staticmethod
    def pos ():
        position = pygame.mouse.get_pos()
        return (position[0], position[1])

    @staticmethod
    def handleEvents (e):
        if e.type == MOUSEBUTTONDOWN:
            Mouse.handleMouseDown()

    @staticmethod
    def handleMouseDown ():
        for o in Mouse.observers:
            o.onClick()

    @staticmethod
    def addObserver (observer):
        Mouse.observers.append (observer)