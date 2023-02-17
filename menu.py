import pygame

from button import Button
from common import WIDTH, HEIGHT, get_font


class MainMenu:
    def __init__(self) -> None:
        super().__init__()
        self.header = get_font(80).render("SPACE SHOOTER", True, "Green")
        self.play = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 - 100),
                           text_input="PLAY", font=get_font(40),
                           base_color="White", hovering_color="Green")
        self.options = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2),
                              text_input="OPTIONS", font=get_font(40),
                              base_color="White", hovering_color="Green")
        self.exit = Button(image=None, pos=(WIDTH / 2, HEIGHT / 2 + 200),
                           text_input="EXIT", font=get_font(40),
                           base_color="White", hovering_color="Green")

    def draw(self, screen: pygame.Surface, mouse_pos: pygame.mouse):
        screen.fill("black")
        screen.blit(self.header, self.header.get_rect(center=(WIDTH/2, 100)))
        for button in [self.play, self.options, self.exit]:
            button.change_color(mouse_pos)
            button.update(screen)

