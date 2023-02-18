import pygame


class Bullet:
    def __init__(self, game):
        self.screen = game.screen
        self.image = pygame.image.load("assets/player_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

    def update(self):
        self.rect.y -= 2

    def draw(self):
        self.screen.blit(self.image, self.rect)
