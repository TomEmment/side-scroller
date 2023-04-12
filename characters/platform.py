import pygame
from tools.background_info import win_height, win_width


class platform:
    def __init__(self, x, y, width, height,  colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.body = pygame.Rect(self.x,
                                self.y,
                                self.width,
                                self.height)
