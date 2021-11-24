import pygame
from . import display


class Events:
    running = True;

    def __init__(self):
        running = True;
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False;

                elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: # If user left clicked
                    for button in display.DisplayManager.buttons:
                       if button.collides(pygame.mouse.get_pos()):
                            button.onClick();
