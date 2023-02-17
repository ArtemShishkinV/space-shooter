import sys

import pygame

from ship import Ship


class Game:
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.ship = Ship(screen)

    def start(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._control(event)

    def _update_screen(self):
        self.screen.fill("black")
        self.ship.blit_me()
        pygame.display.update()

    def _control(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
