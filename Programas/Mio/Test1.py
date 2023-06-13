import pygame
import sys
import math

# Inicializar pygame
pygame.init()

# Configurar la ventana
ventana = pygame.display.set_mode((1280, 640))
pygame.display.set_caption("Mi Juego")

# Cargar la imagen del personaje
mi_imagen = pygame.image.load("Imagenes/pinguino.png")
# Redimensionar la imagen a 130x169 píxeles
mi_imagen = pygame.transform.scale(mi_imagen, (86, 112))
rectangulo1 = mi_imagen.get_rect()
rectangulo1.x = 400
rectangulo1.y = 100

# Crear un suelo
suelo = pygame.Rect(-200, 550, 1500, 200)

#Gravedad
velocidad_y = 6

# LIMITAR VELOCIDAD A 60 FPS
reloj = pygame.time.Clock()


#VARIABLES DE LA bOLA
pinguinoCordX = mi_imagen.get_rect().x
pinguinoCordY = mi_imagen.get_rect().y
xO = pinguinoCordX
yO = pinguinoCordY
relativoBolaX = 0
relativoBolaY = 0
contadorBola = 0
xBola = xO
yBola = yO

x1, y1 = 0, 0
x2, y2 = 0, 0
x3, y3 = 0, 0
a = 0
b = 0
c = 0
h = 0
co = 0
ca = 0
A = 0
B = 0
C = 0
vO = 0
t = 0
g = 0
Arad=0


volteado=False
colisionopiso=False
subir=False

contador=0

lanzarBola=False
instaClick=True
ContadorBoolean=False

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()


    #GRAVEDAD
    rectangulo1.y += velocidad_y
    if rectangulo1.colliderect(suelo):
        velocidad_y = 0
        rectangulo1.y = suelo.y - rectangulo1.height
        colisionopiso=True
    else:
        velocidad_y=6
        colisionopiso=False


    # SALTO
    if teclas[pygame.K_UP] and colisionopiso:
        subir=True
        contador=0

    if subir==True and contador<25 and teclas[pygame.K_UP]:
        velocidad_y-=11.5
    
    contador+=1

    
    #BOLA (Booleans)
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and instaClick:
            lanzarBola = True
            instaClick = False

    if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            instaClick = True


    # Dibujar el fondo
    ventana.fill((255, 255, 255))

    #BOLA (Calculos)
    if(lanzarBola): #Lo que pase aca SOLO pasa en el instante en el que se da el click para la bola

        if(volteado):
            xO = rectangulo1.x+10
            yO = rectangulo1.y+60
        else:
            xO = rectangulo1.x+80
            yO = rectangulo1.y+60
        ContadorBoolean=True
        relativoBolaX, relativoBolaY = pygame.mouse.get_pos()

        (x1, y1) = (relativoBolaX, relativoBolaY)
        (x2, y2) = (xO, yO)
        (x3, y3) = (x1, y2)

        a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        b = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        c = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)

        if a > b and a > c:
            h = a
            co = b
            ca = c
        elif b > a and b > c:
            h = b
            co = a
            ca = c
        else:
            h = c
            co = a
            ca = b

        # Calcula los ángulos de la trayectoria
        A = math.degrees(math.atan(co/ca))
        B = math.degrees(math.atan(ca/co))
        C = 90
        Arad = math.radians(A) #Angulo A en radianes

        
    if(ContadorBoolean): #LO QUE PONGA ACA SE EJECUTA DURANTE MAS O MENOS 1 SEGUNDO
        
        contadorBola+=1
        t+=0.1
        vO=100
        g=5 

        #Decide si se lanza a la izquierda o derecha
        if(relativoBolaX > xO):
            xBola = xO + (vO * math.cos(Arad) * t)
        elif(relativoBolaX < xO):
            xBola = xO - (vO * math.cos(Arad) * t)
        
        #Decide si se lanza hacia arriba o abajo
        if(relativoBolaY > yO):
            yBola = yO + (vO * (math.sin(Arad)) * t) + ((1/2) * g * (t*t))
        elif(relativoBolaY < yO):
            yBola = yO - (vO * (math.sin(Arad)) * t) + ((1/2) * g * (t*t))
        

        print ("vO = ",vO)
        print ("Angulo = ", A)
        print ("Coseno Angulo = ", math.cos(A))
        print ("Seno Angulo = ", math.sin(A))
        print ("Tiempo Transcurrido = ", t)
        print ("xO = ", xO)
        print ("yO = ", yO)
        print ("Xbola = ", xBola)
        print ("Ybola = ", yBola)
        print ("#################################")
    else:
        xBola = xO
        yBola = yO
        t=0
        

    

    if(contadorBola>=100):
         ContadorBoolean=False
         contadorBola=0
         
    lanzarBola = False

    

    

    # Dibujar el suelo
    pygame.draw.rect(ventana, (142, 255, 255), suelo)

    #MOVER AL PINGUINO IZQUIERDA O DERECHA
    if teclas[pygame.K_LEFT]:
        rectangulo1.x -= 5
        volteado=True
    if teclas[pygame.K_RIGHT]:
        rectangulo1.x += 5
        volteado=False
    
    if volteado:
        mi_imagen_flipped = pygame.transform.flip(mi_imagen, True, False)

        ventana.blit(mi_imagen_flipped, rectangulo1)
        if not (ContadorBoolean):
            xBola= rectangulo1.x+10
            yBola = rectangulo1.y+60
        
    else:
        ventana.blit(mi_imagen, rectangulo1)
        if not (ContadorBoolean):
            xBola = rectangulo1.x+80
            yBola = rectangulo1.y+60
    
    # Dibujar la bola
    pygame.draw.circle(ventana, (255, 0, 0), (int(xBola), int(yBola)), 10)




    # Actualizar la pantalla
    pygame.display.update()
    #LIMITAR VELOCIDAD A 120 FPS
    reloj.tick(120)