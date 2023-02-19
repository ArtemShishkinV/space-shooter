import sys

import pygame
from pygame.event import Event

from alien import Alien
from bullet import Bullet
from common import MAX_COUNT_BULLETS, COUNT_ALIENS, HEIGHT
from game_over import GameOver
from ship import Ship


class Game:
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.__new_game()

    def __new_game(self):
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.count = 0
        self.is_end = False
        self.restart = False
        self.to_menu = False

    def start(self):
        self.__generate_aliens()
        while True:
            self.__check_events()
            self.ship.update()
            self.__update_bullets()
            self.__collide_bullets_with_aliens()
            self.__update_aliens()
            game_over = self.__collide_ship_with_aliens()
            if game_over:
                if game_over.is_restart_game:
                    self.__restart_game()
                if game_over.back_to_menu:
                    return
            self.__update_screen()

    def __restart_game(self):
        print("RESTART")
        self.__new_game()
        self.__generate_aliens()

    def __collide_bullets_with_aliens(self):
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)
        count_destroyed = len(collisions)
        self.count += count_destroyed
        for i in range(count_destroyed):
            self.aliens.add_internal(Alien(self, self.aliens))

    def __collide_ship_with_aliens(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.is_end = True
            game_over = GameOver(self)
            game_over.start()
            return game_over

    def __generate_aliens(self):
        for i in range(COUNT_ALIENS):
            self.aliens.add_internal(Alien(self, self.aliens))

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.__control(event)

    def __update_screen(self):
        self.screen.fill("black")
        self.ship.blit_me()
        self.__draw_bullets()
        self.__draw_aliens()
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
            self.bullets.add_internal(Bullet(self, self.bullets))

    def __update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove_internal(bullet)

    def __update_aliens(self):
        self.aliens.update()
        for alien in self.aliens.sprites():
            if alien.rect.top > HEIGHT:
                self.aliens.remove_internal(alien)
                self.aliens.add_internal(Alien(self, self.aliens))

    def __draw_bullets(self):
        self.__draw_groups(self.bullets)

    def __draw_aliens(self):
        self.__draw_groups(self.aliens)

    def __draw_groups(self, sprites):
        for sprite in sprites.sprites():
            sprite.draw()
