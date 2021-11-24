import pygame


class Events:
    def __init__(self):
        running = True;
        while (running):
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False;
