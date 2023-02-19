from random import randint as rnd

import pygame

from utils import WIDTH


class Alien(pygame.sprite.Sprite):
    def __init__(self, game, *groups):
        super().__init__(*groups)
        self.screen = game.screen
        self.image = pygame.image.load(f'assets/enemies/enemy{rnd(1, 5)}.png')
        self.rect = self.image.get_rect()
        self.rect.x = rnd(30, WIDTH - 30)
        self.rect.y = rnd(-800, -50)
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)