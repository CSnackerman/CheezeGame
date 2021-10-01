from config import WIDTH, HEIGHT
from pygame.display import set_mode, set_caption, update
from pygame.locals import DOUBLEBUF

class Window:

    bg_color = '#c27919'
    resolution = (WIDTH, HEIGHT)
    flags = DOUBLEBUF

    def __init__ (self, title):
        self.surface = set_mode (Window.resolution, Window.flags)
        set_caption (title)


    def clear (self):
        self.surface.fill (Window.bg_color)


    def update (self):
        update ()