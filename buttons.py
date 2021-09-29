from pygame import Rect, Color
from pygame import Vector2
import pygame.draw

from config import *
from fonts import Fonts

# base class
class Button:

    def __init__ (self, text_val='BUTTON', x=0, y=0, w=50, h=25, color='#FFFFFF', text_color='#000000'):
        
        self.kind = 'base'
        self.color = Color (color)
        self.position = Vector2 (x, y)
        self.width = w
        self.height = h
        
        self.rect = Rect (x, y, w, h)

        self.font = Fonts.getButtonFont()
        self.textVal = text_val
        self.textColor = text_color
        self.textPosition = Vector2 (x, y)
        self.textWidth = Fonts.getSize (self.font, text_val) [0]
        self.textHeight = Fonts.getSize (self.font, text_val) [1]
        self.textSurface = self.font.render (text_val, True, self.textColor)


    def draw (self, win_surface):
        self.drawRect (win_surface)
        self.drawText (win_surface)


    # utility

    def drawRect (self, win_surface):
        pygame.draw.rect (
            win_surface,
            self.color,
            self.rect,
        )

    def drawText (self, win_surface):
        win_surface.blit ( 
            self.textSurface, 
            (self.textPosition.x, self.textPosition.y)
        )
    

    def bindRect (self):
        self.rect = Rect (
            self.position.x, self.position.y, 
            self.width, self.height
        )

    def bindTextPosition (self):
        horizOffset = (self.width - self.textWidth) // 2
        vertOffset = (self.height - self.textHeight) // 2 
        posX = self.position.x + horizOffset
        posY = self.position.y + vertOffset
        self.textPosition = Vector2 (posX, posY)

    def createTextSurface (self):
        self.textSurface = self.font.render (self.textVal, True, self.textColor)

    def setTextColor (self, c):
        self.textColor = Color (c)




# concrete button implementations

class CenteredButton (Button):
    
    def __init__(self, text_val='BUTTON', x=0, y=0, w=50, h=25, color='#FFFFFF', text_color='#000000'):
        super().__init__(text_val=text_val, x=x, y=y, w=w, h=h, color=color, text_color=text_color)
        self.kind ='centered'
        self.position.x = WIDTH // 2 - self.width // 2
        self.bindRect()
        self.bindTextPosition()
        self.createTextSurface()


class CenteredRoundedButton (CenteredButton):

    def __init__(self, radius, text_val='BUTTON', x=0, y=0, w=50, h=25, color='#FFFFFF', text_color='#000000'):
        super().__init__(text_val=text_val, x=x, y=y, w=w, h=h, color=color, text_color=text_color)
        self.kind = 'centered_rounded'
        self.radius = radius


    def draw (self, win_surface):
        pygame.draw.rect (
            win_surface,
            self.color,
            self.rect,
            border_radius=self.radius
        )
        self.drawText (win_surface)