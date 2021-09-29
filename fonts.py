import pygame.font
from pygame.font import Font
from pygame.font import SysFont

class Fonts:

    # factory methods

    @staticmethod
    def getButtonFont ():
        return SysFont ('ubuntu', 17, True, False)

    # utility
    @staticmethod
    def getSize (font, textVal):
        return Font.size (font, textVal)
    
    

# misc.

def printFonts ():
    fonts = pygame.font.get_fonts()
    num_fonts = len (fonts)
    for i in range (num_fonts):
        print (fonts [i], end='  |  ')
        if i % 3 == 0 and i != 0:
            print ()

def searchFonts (name):
    fonts = pygame.font.get_fonts()
    if name in fonts:
        print (name, 'FOUND')
    else:
        print (name, 'NOT FOUND')



if __name__ == '__main__':
    # printFonts()
    searchFonts ('liberationsans')
    searchFonts ('ubuntu')