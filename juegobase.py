import pygame
import sys
import random

#constantes
ANCHO = 800
ALTO = 600
HotPink = (255,105,180)
colorNegro = (0,0,0)
colorCeleste = (81,209,246)
colorMorado = (191,0,255)


#jugador
jugadorSize = 50
jugadorPosicion = [ANCHO / 2, ALTO - jugadorSize * 2]


#enemigo(s)
enemigo_size = 50
enemigoPos = [random.randint(0, ANCHO - enemigo_size),0]

#ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))


game_over = False
clock = pygame.time.Clock()

#funciones

def detectar_Colision(jugadorPosicion, enemigoPos):
    jx = jugadorPosicion[0]
    jy = jugadorPosicion[1]
    ex = enemigoPos[0]
    ey = enemigoPos[1]
    
    if (ex >= jx and ex <(jx + jugadorSize)) or (jx >= ex and jx < (ex + enemigo_size)):
        if (ey >= jy and ey <(jy + jugadorSize)) or (jy >= ey and jy < (ey + enemigo_size)):
            return True
        return False

while not game_over:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            x = jugadorPosicion[0]
            if event.key == pygame.K_LEFT:
                x -= jugadorSize
            if event.key == pygame.K_RIGHT:
                x += jugadorSize
                
            jugadorPosicion [0] = x
            
    ventana.fill(colorNegro)
    
    if enemigoPos[1] >= 0 and enemigoPos[1]  < ALTO:
        enemigoPos[1] += 20
    else:
        enemigoPos[0] = random.randint(0, ANCHO - enemigo_size)
        enemigoPos[1] = 0
        
    #colisiones
    if detectar_Colision(jugadorPosicion, enemigoPos):
        game_over = True
   
    
    #dibujar enemigo
    pygame.draw.rect(ventana, colorCeleste,
                     (enemigoPos[0], enemigoPos[1], 
                      enemigo_size, enemigo_size))
    
            
     #dibujar jugador
    pygame.draw.rect(ventana, HotPink ,
                     (jugadorPosicion[0],jugadorPosicion[1],
                      jugadorSize,jugadorSize))
    
   
    
    clock.tick(30)
    pygame.display.update()