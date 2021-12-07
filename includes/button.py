import pygame

from includes import events
from includes import display


class Button:
    def __init__(self, display, bg_color, position, size, name):
        self.position = position;
        self.size = size;
        self.name = name;
        pygame.draw.rect(display, bg_color, (position, size), border_radius=10);

    def collides(self, pos):
        if self.position[0] < pos[0] < self.position[0] + self.size[0] and self.position[1] < pos[1] < self.position[1] + self.size[1]:
            return True;
        else:
            return False;

    def onClick(self):
        if self.name == 'START':
            display.DisplayManager().gameScreen();
        elif self.name == 'SETTINGS':
            print('Open settings!');
        elif self.name == 'EXIT':
            events.Events.running = False;