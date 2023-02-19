import sys

import pygame

import menu
from common import WIDTH, HEIGHT
from game import Game


class GameController:
    def __init__(self):
        pygame.init()
        self.menu = menu.MainMenu()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Shooter")

    def start(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.menu.draw(self.screen)
            self._check_events(mouse_pos)
            pygame.display.update()

    def _check_events(self, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_enter_buttons(event)
                self.menu.change_active_button(event)

    def _check_enter_buttons(self, event):
        if event.key == pygame.K_RETURN:
            if self.menu.active == 0:
                game = Game(self.screen)
                game.start()
            if self.menu.active == 2:
                pygame.quit()
                sys.exit()
