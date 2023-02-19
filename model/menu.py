import pygame

from utils import WIDTH, get_font


class Menu:
    def __init__(self, header, buttons) -> None:
        super().__init__()
        self.header = get_font(80).render(header, True, "Green")
        self.buttons = buttons
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
        if len(self.buttons) == self.active + change_value:
            self.active = 0
        elif self.active + change_value == -1:
            self.active = len(self.buttons) - 1
        else:
            self.active += change_value
