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
            self.menu.draw(self.screen, mouse_pos)
            self._check_events(mouse_pos)
            pygame.display.update()

    def _check_events(self, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._check_click_on_buttons(mouse_pos)

    def _check_click_on_buttons(self, mouse_pos):
        if self.menu.play.check_for_input(mouse_pos):
            game = Game(self.screen)
            game.start()
        if self.menu.exit.check_for_input(mouse_pos):
            pygame.quit()
            sys.exit()
