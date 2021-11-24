import pygame


class DisplayManager:
    def __init__(self):
        windowTitle = "4 In Line"

        pygame.init();
        pygame.display.set_mode(size=(600, 600));
        pygame.display.set_caption(windowTitle);