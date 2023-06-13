import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_count = 0

    def update(self, bolas_de_nieve):
        if self.hit_count < 2:
            colisiones = pygame.sprite.spritecollide(self, bolas_de_nieve, True)
            if colisiones:
                self.hit_count += 1
                if self.hit_count == 2:
                    self.kill()
