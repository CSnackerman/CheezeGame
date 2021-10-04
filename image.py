from pygame import Rect
from pygame.color import Color
import pygame.image
import pygame.transform
import pygame.draw

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
        self.dbColor = Color ('#00ff00')

        self.original = pygame.image.load (self.filepath).convert_alpha()
        self.surface = pygame.transform.scale (self.original, (self.w, self.h))

    def draw (self, win_surface):
        win_surface.blit (self.surface, (self.x, self.y))

    def debugDraw (self, win_surface):
        pygame.draw.rect (win_surface, self.dbColor, self.rect)
        self.draw (win_surface)


    def move (self, dx, dy):
        self.x += dx * Time.dt
        self.y += dy * Time.dt
        self.rect.update (self.x, self.y, self.w, self.h)

    def moveTo (self, x, y):
        self.x = x
        self.y = y
        self.rect.update (x, y, self.w, self.h)

    def resize (self, w, h):
        self.w = w
        self.h = h
        self.rect.w = w
        self.rect.h = h
        self.surface = pygame.transform.scale (self.original, (w, h))

