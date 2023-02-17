import pygame


class Ship:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 1
