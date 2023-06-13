import pygame
import math
from main import player
from main import spritesheet
from main import map
from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola
from palancas import Palanca


###################### Nivel 1 ######################

#Fase 1
palanca1 = Palanca(1150, 192, 66, 66)
#Fase 2
palanca2 = Palanca(1152, 320, 64, 64)
palanca3 = Palanca(576, 64, 64, 64)


def detectarColisionesConstantemente():
    if palanca1.detect_collision(player.bola):
        print("HOLA")
        map = TileMap('Niveles/Nivel1-1CLEAN.csv', spritesheet )


