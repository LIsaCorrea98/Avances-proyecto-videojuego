from tiles import *
from spritesheet import Spritesheet
from player import Player, Bola

# Cargar una ventana y un reloj interno
pygame.init()
DISPLAY_W, DISPLAY_H = 1280, 640
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
TARGET_FPS = 60

# Cargar las imagenes y el spritesheet
spritesheet = Spritesheet('spritesheet.png')
player = Player()

# Cargar el nivel
map = TileMap('Niveles/Nivel1-1.csv', spritesheet)

player.position.x, player.position.y = map.start_x, map.start_y
player.bola = Bola(player.position, player.velocity, player)

# Bucle principal del juego
while running:
    dt = clock.tick(120) * 0.001 * TARGET_FPS

    # Checar el input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.LEFT_KEY, player.FACING_LEFT = True, True
            elif event.key == pygame.K_d:
                player.RIGHT_KEY, player.FACING_LEFT = True, False
            elif event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.LEFT_KEY = False
            elif event.key == pygame.K_d:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= .25
                    player.is_jumping = False

    # Actualizar / Animar Sprites
    player.update(dt, map.tiles)
    player.bola.update(dt, player.position)

    # Actualizar ventana
    canvas.fill((0, 180, 240))  # Llena la ventana de azul
    map.draw_map(canvas)

    player.draw(canvas)
    player.bola.draw(canvas)
    window.blit(canvas, (0, 0))
    pygame.display.update()
