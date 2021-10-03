from pygame.rect import Rect
from pygame.surface import Surface
from pygame.color import Color
from pygame.locals import *

class Banner:

    scroll_speed = 50

    def __init__ (self, x, y, w, h, bgcolor, items:list):

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.bgColor = Color (bgcolor)
        self.clipRect = Rect (x, y, w, h)

        self.surface = Surface ((w, h), SRCALPHA)

        self.numItems = len (items)
        self.totalItemWidth = 0
        self.itemMargin = 25 # px
        self.itemWidth = h // 4 * 3
        self.itemHeight = self.itemWidth

        self.items = []
        for item in items:
            self.addItem (item)


    def draw (self, win_surface):

        self.surface.fill (self.bgColor)

        self.scrollItems ()
        
        for item in self.items:
            self.surface.blit (item.surface, (item.x, item.y))
        
        win_surface.blit (self.surface, (self.x, self.y))

    

    def addItem (self, item):
        self.numItems += 1
        item.resize (self.itemWidth, self.itemHeight)
        centerY = self.h // 2 - item.h // 2
        item.moveTo (self.totalItemWidth + self.itemMargin, centerY)
        self.totalItemWidth += self.itemWidth + self.itemMargin
        self.items.append (item)

    def scrollItems (self):
        for item in self.items:
            item.move (Banner.scroll_speed, 0)

            if self.totalItemWidth < self.w:
                if item.x > self.w:
                    item.moveTo (-item.w, item.y)

            else:
                if item.x > self.totalItemWidth:
                    item.moveTo (-item.w, item.y)
                
