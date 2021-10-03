from pygame import Rect
import pygame.image
import pygame.transform
from os import path

from timez import Time

class Image:

    def __init__ (self, filename, x, y, w, h):

        self.filepath = path.join ('images', filename)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.rect = Rect (x, y, w, h)

        self.original = pygame.image.load (self.filepath).convert_alpha()
        self.surface = pygame.transform.scale (self.original, (self.w, self.h))

    def draw (self, win_surface):
        win_surface.blit (self.surface, (self.x, self.y))

    def move (self, dx, dy):
        self.x += dx * Time.dt
        self.y += dy * Time.dt
        self.rect.move_ip (self.x, self.y)

    def moveTo (self, x, y):
        self.x = x
        self.y = y
        self.rect.move_ip (x, y)

    def resize (self, w, h):
        self.w = w
        self.h = h
        self.rect.w = w
        self.rect.h = h
        self.surface = pygame.transform.scale (self.original, (w, h))

