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
    for _ in range (3):
        bannerItems.append (Image ('cheeze.png', 0,0,0,0))

    banner1 = Banner (
        50, 50, 
        WIDTH - 100, 100,
        '#333333', 
        bannerItems
    )

    bannerItems = []
    for _ in range (7):
        bannerItems.append (Image ('cheeze.png', 0,0,0,0))

    banner2 = Banner (
        50, 200, 
        WIDTH - 100, 150,
        '#333333', 
        bannerItems
    )



    
    while 1:
        Time.handleTime()
        EventHandler.pollEvents()
        window.clear()

        banner1.draw (window.surface)
        banner2.draw (window.surface)

        window.update()



# choose a test to run by uncommenting

# test_Image()
test_Banner()




pygame.quit()