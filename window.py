from config import WIDTH, HEIGHT
from pygame.display import set_mode, set_caption, update
from pygame.locals import DOUBLEBUF
from timez import Time

class Window:

    bg_color = '#a83800'
    resolution = (WIDTH, HEIGHT)
    flags = DOUBLEBUF

    def __init__ (self, title):
        self.surface = set_mode (Window.resolution, Window.flags)
        self.title = title
        set_caption (title)


    def clear (self):
        self.surface.fill (Window.bg_color)


    def update (self):
        update ()
        set_caption (self.title + ' - ' + Time.getFPS() + ' FPS')
