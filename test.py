import pygame
from config import WIDTH

from window import Window
from timez import Time
from events import EventHandler
from image import Image
from banner import Banner

pygame.init()

def test_Image():
    window = Window ('TEST CenteredButton')
    img = Image ('cheeze.png', 0, 0, 100, 100)
    
    while 1:
        Time.handleTime()
        EventHandler.pollEvents()
        window.clear()
        img.move (100, 0)
        img.draw (window.surface)
        window.update()


def test_Banner ():
    window = Window ('TEST CenteredButton')

    bannerItems = []
    for i in range (10):
        bannerItems.append (Image ('cheeze.png', 0,0,0,0))

    banner = Banner (
        50, 50, 
        WIDTH - 100, 100,
        '#000000', 
        bannerItems
    )

    banner.addItem (Image ('cheeze.png', 0,0,0,0))
    
    while 1:
        Time.handleTime()
        EventHandler.pollEvents()
        window.clear()

        banner.draw (window.surface)

        window.update()



# choose a test to run by uncommenting

# test_Image()
test_Banner()




pygame.quit()