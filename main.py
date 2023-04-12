from tools.colours import red, white, black, blue
from tools.fonts import Mediumfont
from tools.background_info import win_height, win_width
from characters.player import player
from characters.platform import platform
import pygame
pygame.init()


main_character = player(10, 10, red)

platform1 = platform(500, 500, 100, 10, blue)
platform2 = platform(300, 350, 100, 10, blue)
platform3 = platform(550, 250, 100, 10, blue)

platforms = [platform1, platform2, platform3]

run = True


win = pygame.display.set_mode((win_width, win_height))
while run:
    pygame.time.delay(50)
    collision = False
    collision_body = None

    win.fill(black)

    for active_platform in platforms:
        pygame.draw.rect(win,
                         active_platform.colour,
                         active_platform.body)
    for active_platform in platforms:
        possible_collision = main_character.body.colliderect(
            active_platform.body)
        if possible_collision:
            collision = True
            collision_body = active_platform.body

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    main_character.movement_logic(keys, collision, collision_body)
    pygame.draw.rect(win,
                     main_character.colour,
                     main_character.body)

    pygame.display.update()
