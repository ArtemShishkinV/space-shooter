import pygame


class Ship:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 5
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
