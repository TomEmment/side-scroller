import pygame
from tools.background_info import win_height, win_width


class player:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.colour = colour
        self.velocity = 10
        self.is_jumping = False
        self.jump_count = 10
        self.body = pygame.Rect(self.x,
                                self.y,
                                self.width,
                                self.height)

    def movement_logic(self, keys, collision, collision_body=None):
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity

        if keys[pygame.K_LEFT]:
            self.x -= self.velocity

        if self.is_jumping:
            if self.jump_count >= -10 and not (self.jump_count <= 0 and not collision):
                self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jumping = False
        else:
            if keys[pygame.K_SPACE] and (collision or self.y == win_height - self.width):
                self.is_jumping = True

            if self.y + self.height < win_height and not collision:
                self.y += self.velocity

        if self.x >= win_width - self.width:
            self.x = win_width - self.width
        if self.x < 0:
            self.x = 0
        if collision:
            if self.y > collision_body.y - self.height:
                self.y = collision_body.y - self.height + 1
        else:
            if self.y >= win_height - self.height:
                self.y = win_height - self.height

        self.body = pygame.Rect(self.x,
                                self.y,
                                self.width,
                                self.height)
