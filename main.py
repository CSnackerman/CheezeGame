import pygame

from window import Window
from events import EventHandler
from menu import Menu

# --- Setup ---
pygame.init()
window = Window ('Wise Cheeze')

# scenes
menu = Menu()


# --- Main Loop ---
while 1:

    EventHandler.pollEvents()
    window.clear()
    menu.display (window.surface)
    window.update()
