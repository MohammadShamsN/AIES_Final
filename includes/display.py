import pygame
import os
from . import button


class DisplayManager:
    windowTitle = "4 In Line"
    screen_width, screen_height = 600, 600;
    display = None;
    font = None;
    bg = None;
    buttons = [];

    def __init__(self):
        pygame.font.init();
        self.bg = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../textures/background.jpg"))
        self.font = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../fonts/Quicksand-Regular.ttf"), 20);

        pygame.init();
        pygame.display.set_caption(self.windowTitle);
        self.display = pygame.display.set_mode(size=(self.screen_width, self.screen_height));
        pygame.display.get_surface()
        # Get display

    def mainMenu(self):
        self.buttons.clear();
        btn_width, btn_height = 175, 40;
        btn_color = (125, 0, 125);
        text_color = (255, 255, 255);
        pygame.display.set_caption(self.windowTitle + " - Main Menu");

        self.display.blit(self.bg, (-300, -200));
        btn_start = button.Button(self.display, btn_color, ((self.screen_width - btn_width) / 2, 350), (btn_width, btn_height), 'START'); # Start game
        txt_width, txt_height = pygame.font.Font.size(self.font, "Start Game");
        self.display.blit(pygame.font.Font.render(self.font, "Start Game", True, text_color, None),
                          dest=((self.screen_width - txt_width) / 2, 350 + (btn_height - txt_height) / 2));
        self.buttons.append(btn_start);

        btn_settings = button.Button(self.display, btn_color, ((self.screen_width - btn_width) / 2, 400), (btn_width, btn_height), 'SETTINGS'); # Settings
        txt_width, txt_height = pygame.font.Font.size(self.font, "Settings");
        self.display.blit(pygame.font.Font.render(self.font, "Settings", True, text_color, None),
                          dest=((self.screen_width - txt_width) / 2, 400 + (btn_height - txt_height) / 2));
        self.buttons.append(btn_settings);

        btn_exit = button.Button(self.display, btn_color, ((self.screen_width - btn_width) / 2, 450), (btn_width, btn_height), 'EXIT'); # Exit
        txt_width, txt_height = pygame.font.Font.size(self.font, "Exit");
        self.display.blit(pygame.font.Font.render(self.font, "Exit", True, text_color, None),
                          dest=((self.screen_width - txt_width) / 2, 450 + (btn_height - txt_height) / 2));
        self.buttons.append(btn_exit);

        pygame.display.update()

    def gameScreen(self):
        self.display.fill((0, 0, 0));
        self.buttons.clear();
        pygame.display.set_caption(self.windowTitle + " - Game");

        pygame.display.update()