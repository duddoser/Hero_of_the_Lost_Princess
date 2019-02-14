import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 640))
clock = pygame.time.Clock()


def death_screen():
    intro_text = ["YOU ARE DEAD",
                  "Press space to continue", ]
    screen.fill((0, 0, 0))
    fon = pygame.Surface(screen.get_size())
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    string_rendered1 = font.render(intro_text[0], 1, pygame.Color('white'))
    intro_rect1 = string_rendered1.get_rect()
    intro_rect1.top = 250
    intro_rect1.x = 275
    screen.blit(string_rendered1, intro_rect1)
    string_rendered2 = font.render(intro_text[1], 1, pygame.Color('white'))
    intro_rect2 = string_rendered2.get_rect()
    intro_rect2.top = 500
    intro_rect2.x = 210
    screen.blit(string_rendered2, intro_rect2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(60)

death_screen()
