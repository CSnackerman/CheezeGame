import pygame.image
from os import path

class Image:

    def __init__ (self, filename, x, y, w, h):

        self.filepath = path.join ('images', filename)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.surface = pygame.image.load (self.filepath)
