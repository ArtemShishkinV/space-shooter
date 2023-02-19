import sys

import pygame

from common import get_font, WIDTH, get_game_over_menu_buttons
from menu import Menu


class GameOver:
    def __init__(self, game):
        self.header = get_font(80).render("GAME OVER", True, "Green")
        self.menu = Menu("GAME OVER", get_game_over_menu_buttons())
        self.screen = game.screen
        self.count = game.count
        self.is_restart_game = False
        self.back_to_menu = False

    def start(self):
        while True:
            self.screen.fill("black")
            self.screen.blit(self.header, self.header.get_rect(center=(WIDTH / 2, 100)))
            self.menu.draw(self.screen)
            self._check_events()
            if self.is_restart_game or self.back_to_menu:
                return
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
                self.is_restart_game = True
            if self.menu.active == 1:
                self.back_to_menu = True
