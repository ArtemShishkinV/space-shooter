import pygame

from button import Button


def get_font(size):
    return pygame.font.Font("assets/space_invaders.ttf", size)


WIDTH = 1280
HEIGHT = 720
MAX_COUNT_BULLETS = 3
COUNT_ALIENS = 6


def get_main_menu_buttons():
    return [
        Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 - 100),
               text_input="PLAY", font=get_font(40),
               base_color="White", hovering_color="Green"),
        Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 50),
               text_input="OPTIONS", font=get_font(40),
               base_color="White", hovering_color="Green"),
        Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 200),
               text_input="EXIT", font=get_font(40),
               base_color="White", hovering_color="Green")
    ]


def get_game_over_menu_buttons():
    return [
        Button(image=None, pos=(WIDTH / 2, HEIGHT / 2),
               text_input="TRY AGAIN", font=get_font(40),
               base_color="White", hovering_color="Green"),
        Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 100),
               text_input="BACK TO MENU", font=get_font(40),
               base_color="White", hovering_color="Green")
    ]

# GAME_OVER_MENU_BUTTONS = [
#     Button(image=None, pos=(WIDTH / 2, HEIGHT / 2),
#            text_input="TRY AGAIN", font=get_font(40),
#            base_color="White", hovering_color="Green"),
#     Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 100),
#            text_input="BACK TO MENU", font=get_font(40),
#            base_color="White", hovering_color="Green")
# ]
