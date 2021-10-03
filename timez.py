import pygame.time
from config import FRAME_CAP, WAIT_TIME
from math import floor

class Time:
    
    clock = pygame.time.Clock()
    dt = 0
    fps = '0'
    accumulator = 0
    fpsCalcInterval = 250

    @staticmethod
    def handleTime():
        Time.wait (WAIT_TIME)
        Time.dt = Time.tick()
        Time.accumulator += Time.dt
        Time.calculateFPS ()


    @staticmethod
    def tick ():        
        return Time.clock.tick (FRAME_CAP)

    @staticmethod
    def getFPS ():
        return Time.fps
    
    @staticmethod
    def calculateFPS ():
        if Time.accumulator > Time.fpsCalcInterval:
            Time.fps = str ( floor (Time.clock.get_fps()))
            Time.accumulator = 0

    @staticmethod
    def wait (ms):
        pygame.time.wait (ms)