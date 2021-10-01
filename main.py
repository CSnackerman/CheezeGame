import pygame

from window import Window
from events import EventHandler
from menu import Menu
from timez import Time

# --- Setup ---
pygame.init()
window = Window ('Wize Cheeze')

# scenes
menu = Menu()


# --- Main Loop ---
while 1:

    Time.handleTime()
    EventHandler.pollEvents()
    window.clear()
    menu.display (window.surface)
    window.update()
