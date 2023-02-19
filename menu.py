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
        self.buttons = [self.play, self.options, self.exit]
        self.active = 0

    def draw(self, screen: pygame.Surface):
        screen.fill("black")
        screen.blit(self.header, self.header.get_rect(center=(WIDTH/2, 100)))
        for i in range(len(self.buttons)):
            self.buttons[i].change_to_hovering_color(i == self.active)
            self.buttons[i].update(screen)

    def change_active_button(self, event: pygame.event.Event):
        if event.key == pygame.K_DOWN:
            self.change_active_button_value(1)
        elif event.key == pygame.K_UP:
            self.change_active_button_value(-1)

    def change_active_button_value(self, change_value):
        print(self.active)
        if len(self.buttons) == self.active + change_value:
            self.active = 0
        elif self.active + change_value == -1:
            self.active = 2
        else:
            self.active += change_value
