import sys

import pygame

from pygame.event import Event
from ship import Ship


class Game:
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.ship = Ship(screen)

    def start(self):
        while True:
            self.__check_events()
            self.ship.update()
            self.__update_screen()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.__control(event)

    def __update_screen(self):
        self.screen.fill("black")
        self.ship.blit_me()
        pygame.display.update()

    def __control(self, event: Event):
        if event.type == pygame.KEYDOWN:
            self.__control_keys_press(event, True)
        if event.type == pygame.KEYUP:
            self.__control_keys_press(event, False)

    def __control_keys_press(self, event: Event, is_pressed: bool):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = is_pressed
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = is_pressed
