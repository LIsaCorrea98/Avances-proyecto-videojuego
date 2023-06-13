import pygame
import math
from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola

class Palanca:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def detect_collision(self, bola):
        bola_rect = pygame.Rect(bola.xBola, bola.yBola, bola.radius * 2, bola.radius * 2)
        palanca_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bola_rect.colliderect(palanca_rect)
    
    