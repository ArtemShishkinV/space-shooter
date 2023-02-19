import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, *groups):
        super().__init__(*groups)
        self.screen = game.screen
        self.image = pygame.image.load("assets/player_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

    def update(self):
        self.rect.y -= 2

    def draw(self):
        self.screen.blit(self.image, self.rect)
