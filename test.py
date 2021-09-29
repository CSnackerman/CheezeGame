import pygame

from config import HEIGHT
from buttons import CenteredButton, CenteredRoundedButton

from window import Window
from events import EventHandler

pygame.init()

def test_CenteredButton ():
    window = Window ('TEST CenteredButton')
    cb = CenteredButton ('centered', 0, 100, w=100)
    while 1:
        EventHandler.pollEvents()
        window.clear()
        cb.draw (window.surface)
        window.update()


def test_CenteredRoundedButton ():
    window = Window ('TEST CenteredRoundedButton')
    crb = CenteredRoundedButton (25, 'rounded', 0, 50, w=100)
    while 1:
        EventHandler.pollEvents()
        window.clear()
        crb.draw (window.surface)
        window.update()


# choose a test to run by uncommenting

# test_CenteredButton()
# test_CenteredRoundedButton()





pygame.quit()