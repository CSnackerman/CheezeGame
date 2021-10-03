import pygame

from config import HEIGHT

from window import Window
from timez import Time
from events import EventHandler
from image import Image

pygame.init()

def test_Image():
    window = Window ('TEST CenteredButton')
    img = Image ('cheeze.png', 50, 50, 200, 200)
    
    while 1:
        Time.handleTime()
        EventHandler.pollEvents()
        window.clear()
        img.draw (window.surface)
        window.update()



# choose a test to run by uncommenting

test_Image()





pygame.quit()