from tools.colours import red, white, black, blue
from tools.fonts import Mediumfont
from tools.background_info import win_height, win_width
from characters.player import player
from characters.platform import platform
import pygame
import random
pygame.init()


main_character = player(0, win_height, red)

platform1 = platform(random.randint(0, win_width),
                     random.randint(40, (win_height*0.1)),
                     random.randint(50, 200), 10, blue)
platform2 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.1, win_height*0.2),
                     random.randint(50, 200), 10, blue)
platform3 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.2, win_height*0.3),
                     random.randint(50, 200), 10, blue)
platform4 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.3, win_height*0.4),
                     random.randint(50, 200), 10, blue)
platform5 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.4, win_height*0.5),
                     random.randint(50, 200), 10, blue)
platform6 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.5, win_height*0.6),
                     random.randint(50, 200), 10, blue)
platform7 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.6, win_height*0.7),
                     random.randint(50, 200), 10, blue)
platform8 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.7, win_height*0.8),
                     random.randint(50, 200), 10, blue)
platform9 = platform(random.randint(0, win_width),
                     random.randint(win_height*0.8, win_height*0.9),
                     random.randint(50, 200), 10, blue)
platform10 = platform(random.randint(0, win_width),
                      random.randint(win_height*0.9, win_height),
                      random.randint(50, 200), 10, blue)
platforms = [platform1, platform2, platform3, platform4, platform5,
             platform6, platform7, platform8, platform9, platform10]

run = True

score = 0
y_increase = 0
score_threshold = win_height*0.4
win = pygame.display.set_mode((win_width, win_height))
while run:
    pygame.time.delay(50)
    collision = False
    collision_body = None
    reset_platform = False
    win.fill(black)

    if score > 0 and main_character.y == win_height - main_character.height:
        run = False

    if main_character.y <= score_threshold:
        score += (score_threshold - main_character.y)
        for active_platform in platforms:
            active_platform.y += (score_threshold - main_character.y)

            active_platform.body_update()
        main_character.y = score_threshold
    text = Mediumfont.render("Score: "+str(score), True, white)
    win.blit(text, (10, 30))

    for active_platform in platforms:
        if active_platform.y > win_height-10 and not reset_platform:
            active_platform.x = random.randint(0, win_width)
            active_platform.y = 40
            active_platform.width = random.randint(50, 200)
            reset_platform = True
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
