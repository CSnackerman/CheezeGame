import pygame.image
import pygame.transform
from os import path

class Image:

    def __init__ (self, filename, x, y, w, h):

        self.filepath = path.join ('images', filename)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.surface = pygame.image.load (self.filepath).convert_alpha()
        self.surface = pygame.transform.scale (self.surface, (self.w, self.h))

    def draw (self, win_surface):
        win_surface.blit (self.surface, (self.x, self.y))

