import sys

import pygame
from pygame.event import Event

from bullet import Bullet
from common import MAX_COUNT_BULLETS
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
            self.__update_bullets()
            self.__update_screen()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.__control(event)

    def __update_screen(self):
        self.screen.fill("black")
        self.ship.blit_me()
        self.__draw_bullets()
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
        if event.key == pygame.K_SPACE and len(self.bullets) <= MAX_COUNT_BULLETS:
            self.bullets.add_internal(Bullet(self))

    def __update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove_internal(bullet)

    def __draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw()
