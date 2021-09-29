import pygame

from window import Window
from events import EventHandler
from menu import Menu


pygame.init()

window = Window ('Cheeze of Wisdom')


# scenes
menu = Menu()


# main loop
while 1:

    EventHandler.pollEvents()

    window.clear()

    menu.display (window.surface)

    window.update()
