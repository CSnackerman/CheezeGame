from pygame import Rect, Color, init
from pygame import Vector2
import pygame.draw

from config import *
from fonts import Fonts
from utility import *
from mouse import Mouse
from math import pi, sin, cos

# --- Base Button ---

class Button:

    def __init__ (self, x, y, w, h, bgcolor, fgcolor, hovercolor):
        
        self.kind = 'base_button'
        self.position = Vector2 (x, y)
        self.center = Vector2 (x + w // 2, y + h // 2)
        self.width = w
        self.height = h

        self.rect = Rect (x, y, w, h)
        self.bgColor = Color (bgcolor)
        self.fgColor = Color (fgcolor)
        
        self.hoverColor = Color (hovercolor)
        self.isHovered = False

        self.clickListener = None


    def draw (self, win_surface):
        self.drawRect (win_surface)

    def onClick (self):
        if self.rect.collidepoint (Mouse.pos()):
            self.clickListener()

    def onHover (self):
        if self.rect.collidepoint (Mouse.pos()):
            if not self.isHovered:
                self.isHovered = True
        elif self.isHovered:
            self.isHovered = False
        
        
        
    # button utility

    def drawRect (self, win_surface):
        if not self.isHovered:
            pygame.draw.rect (win_surface, self.bgColor, self.rect)
        else:
            pygame.draw.rect (win_surface, self.hoverColor, self.rect)

    def bindRect (self):
        self.rect = Rect (
            self.position.x, self.position.y, 
            self.width, self.height
        )

    def addClickListener (self, listener):
        Mouse.addObserver (self)
        self.clickListener = listener


# --- Rectangular Buttons    

class TextButton (Button):

    def __init__(self, text, x, y, w, h, bgcolor, fgcolor, hovercolor):
        super().__init__(x, y, w, h, bgcolor, fgcolor, hovercolor)

        self.kind = 'text_button'
        self.text = text
        self.font = Fonts.getButtonFont()
        self.textWidth = Fonts.getSize (self.font, text) [0]
        self.textHeight = Fonts.getSize (self.font, text) [1]
        self.textSurface = None
        self.createTextSurface()
        self.textPosition = None
        self.centerTextPosition()
        

    def draw (self, win_surface):
        self.drawRect (win_surface)
        self.drawText (win_surface)


    # text button utility

    def drawText (self, win_surface):
        text_position = (self.textPosition.x, self.textPosition.y)
        win_surface.blit (self.textSurface, text_position)

    def centerTextPosition (self):
        horizOffset = (self.width - self.textWidth) // 2
        vertOffset = (self.height - self.textHeight) // 2 
        posX = self.position.x + horizOffset
        posY = self.position.y + vertOffset
        self.textPosition = Vector2 (posX, posY)

    def createTextSurface (self):
        self.textSurface = self.font.render (self.text, True, self.fgColor)

    

class CenteredTextButton (TextButton):
    
    def __init__(self, text, x, y, w, h, bgcolor, fgcolor, hovercolor):
        super().__init__(text, x, y, w, h, bgcolor, fgcolor, hovercolor)

        self.kind ='centered_text_button'
        self.position.x = WIDTH // 2 - self.width // 2
        self.bindRect()
        self.centerTextPosition()
        self.createTextSurface()



class CenteredRoundedTextButton (CenteredTextButton):

    def __init__(self, text, x, y, w, h, r, bgcolor, fgcolor, hovercolor):
        super().__init__(text, x, y, w, h, bgcolor, fgcolor, hovercolor)
        self.kind = 'centered_rounded_text_button'
        self.radius = r


    def draw (self, win_surface):

        self.drawRoundedRect(win_surface)
        self.drawText (win_surface)

    def drawRoundedRect (self, win_surface):
        if not self.isHovered:
            pygame.draw.rect (
                win_surface, self.bgColor, self.rect, 0, self.radius
            )
        else:
            pygame.draw.rect (
                win_surface, self.hoverColor, self.rect, 0, self.radius
            )





# --- Circular Buttons ---

class CircleButton (Button):

    def __init__(self, x, y, r, bgcolor, fgcolor, hovercolor):
        super().__init__(x, y, r * 2, r * 2, bgcolor, fgcolor, hovercolor)
        self.radius = r


    def draw (self, win_surface):
        c = (self.center.x, self.center.y)
        if not self.isHovered:
            pygame.draw.circle (win_surface, self.bgColor, c, self.radius)
        else:
            pygame.draw.circle (win_surface, self.hoverColor, c, self.radius)
        


class ExitButton (CircleButton):

    def __init__(self, x, y, r, bgcolor, fgcolor, hovercolor):
        super().__init__(x, y, r, bgcolor, fgcolor, hovercolor)

        xRadius = self.radius - 10
        cX = self.center.x
        cY = self.center.y

        self.topright = Vector2 (
                            cX + xRadius * cos (pi / 4),
                            cY + xRadius * sin (pi / 4)
                        )
        self.topleft = Vector2 (
                            cX + xRadius * cos (3 * pi / 4),
                            cY + xRadius * sin (3 * pi / 4)
                        )
        self.botleft = Vector2 (
                            cX + xRadius * cos (5 * pi / 4),
                            cY + xRadius * sin (5 * pi / 4)
                        )
        self.botright = Vector2 (
                            cX + xRadius * cos (7 * pi / 4),
                            cY + xRadius * sin (7 * pi / 4)
                        )


    def draw (self, win_surface):
        super().draw (win_surface)
        pygame.draw.line (win_surface, self.fgColor, self.topleft, self.botright, 7)
        pygame.draw.line (win_surface, self.fgColor, self.botleft, self.topright, 7)