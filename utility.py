from config import *
from math import floor

def pcToPx_horiz (percent):
    return floor (WIDTH * percent / 100)

def pcToPx_vert (percent):
    return floor (HEIGHT * percent / 100)