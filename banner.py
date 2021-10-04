from pygame.rect import Rect
from pygame.surface import Surface
from pygame.color import Color
from pygame.locals import *

class Banner:

    scroll_speed = 100

    def __init__ (self, x, y, w, h, bgcolor, items:list):

        self.debug = False

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.bgColor = Color (bgcolor)
        if not self.debug:
            self.bgColor.a = 0
        self.clipRect = Rect (x, y, w, h)

        self.surface = Surface ((w, h), SRCALPHA)

        self.totalItems = len (items)
        self.totalItemWidth = 0
        self.itemMargin = 25 # px
        self.itemWidth = h // 4 * 3
        self.itemHeight = self.itemWidth

        if self.totalItems * (self.itemWidth + self.itemMargin) < self.w:
            self.calculateMargin ()

        self.itemCounter = 0
        self.items = []
        for item in items:
            self.addItem (item)


    def draw (self, win_surface):

        self.surface.fill (self.bgColor)

        self.scrollItems ()
        
        for item in self.items:
            item.draw(self.surface)
        
        win_surface.blit (self.surface, (self.x, self.y))

    

    def addItem (self, item):
        item.resize (self.itemWidth, self.itemHeight)
        centerY = self.h // 2 - item.h // 2
        item.moveTo (self.totalItemWidth, centerY)
        self.totalItemWidth += self.itemWidth + self.itemMargin
        self.items.append (item)
        self.itemCounter += 1
        
    def scrollItems (self):
        for item in self.items:
            if item.x > self.totalItemWidth:
                print (item.x + item.w, self.totalItemWidth)
                item.moveTo (-item.w, item.y)
                
            item.move (Banner.scroll_speed, 0)


    def calculateMargin (self):
        totalMarginSpace = self.w - self.totalItems * self.itemWidth
        self.itemMargin = totalMarginSpace // self.totalItems