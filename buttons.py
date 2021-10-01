from pygame import Rect, Color
from pygame import Vector2
import pygame.draw

from config import *
from fonts import Fonts
from utility import *
from math import pi, sin, cos

# base class
class Button:

    def __init__ (self, text_val='BUTTON', x=0, y=0, w=100, h=25, color='#FFFFFF', text_color='#000000'):
        
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
        self.bindTextPosition()


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
    
    def __init__(self, text_val='BUTTON', x=0, y=0, w=100, h=25, color='#FFFFFF', text_color='#000000'):
        super().__init__(text_val=text_val, x=x, y=y, w=w, h=h, color=color, text_color=text_color)
        self.kind ='centered'
        self.position.x = WIDTH // 2 - self.width // 2
        self.bindRect()
        self.bindTextPosition()
        self.createTextSurface()


class CenteredRoundedButton (CenteredButton):

    def __init__(self, radius, text_val='BUTTON', x=0, y=0, w=100, h=25, color='#FFFFFF', text_color='#000000'):
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







class CircleButton:

    def __init__ (self, text, x, y, radius, bgcolor, fgcolor):
        
        self.text = text
        self.x = x
        self.y = y
        self.radius = radius
        self.bgColor = Color (bgcolor)
        self.fgColor = Color (fgcolor)
        
        self.hitbox = Rect (
                        x - radius,
                        y - radius,
                        radius * 2,
                        radius * 2
                    )

    def draw (self, win_surface):
        center = (self.x, self.y)
        pygame.draw.circle (win_surface, self.bgColor, center, self.radius)
        




class ExitButton (CircleButton):

    def __init__(self, text, x, y, radius, bgcolor, fgcolor):
        super().__init__(text, x, y, radius, bgcolor, fgcolor)

        xRadius = self.radius - 10

        self.topright = Vector2 (
                            self.x + xRadius * cos (pi / 4),
                            self.y + xRadius * sin (pi / 4)
                        )
        self.topleft = Vector2 (
                            self.x + xRadius * cos (3 * pi / 4),
                            self.y + xRadius * sin (3 * pi / 4)
                        )
        self.botleft = Vector2 (
                            self.x + xRadius * cos (5 * pi / 4),
                            self.y + xRadius * sin (5 * pi / 4)
                        )
        self.botright = Vector2 (
                            self.x + xRadius * cos (7 * pi / 4),
                            self.y + xRadius * sin (7 * pi / 4)
                        )

    def draw (self, win_surface):
        super().draw (win_surface)
        pygame.draw.line (win_surface, self.fgColor, self.topleft, self.botright, 7)
        pygame.draw.line (win_surface, self.fgColor, self.botleft, self.topright, 7)
        
        