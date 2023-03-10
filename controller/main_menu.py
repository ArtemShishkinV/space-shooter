import sys

import pygame

from controller import Game
from model import menu
from utils import WIDTH, HEIGHT, get_main_menu_buttons


class MainMenu:
    def __init__(self):
        pygame.init()
        self.menu = menu.Menu("SPACE SHOOTER", get_main_menu_buttons())
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Shooter")

    def start(self):
        while True:
            self.menu.draw(self.screen)
            self._check_events()
            pygame.display.update()

    def _check_events(self):
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
