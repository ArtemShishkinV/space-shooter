import sys

import pygame

from pygame.event import Event

from bullet import Bullet
from ship import Ship


class Game:
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.ship = Ship(screen)
        self.bullets = pygame.sprite.Group()

    def start(self):
        while True:
            self.__check_events()
            self.ship.update()
            self.__update_screen()
            self.bullets.update()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.__control(event)

    def __update_screen(self):
        self.screen.fill("black")
        self.ship.blit_me()
        for bullet in self.bullets.sprites():
            bullet.draw()
        pygame.display.update()

    def __control(self, event: Event):
        if event.type == pygame.KEYDOWN:
            self.__control_move_keys_press(event, True)
            self.__control_fire(event)
        if event.type == pygame.KEYUP:
            self.__control_move_keys_press(event, False)

    def __control_move_keys_press(self, event: Event, is_pressed: bool):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = is_pressed
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = is_pressed

    def __control_fire(self, event: Event):
        if event.key == pygame.K_SPACE:
            self.bullets.add_internal(Bullet(self))
