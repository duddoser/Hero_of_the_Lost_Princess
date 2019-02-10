import os

import pygame
import pyganim

from player import Hero
from camera import Camera
from platform import draw_level
from sounds import Sounds

pygame.init()
size = width, height = 800, 640
screen = pygame.display.set_mode(size)
pygame.display.flip()

camera = Camera(width, height)
hero_sprite = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
draw_level("1", 32, 32, platform_sprites, all_sprites)
hero = Hero(hero_sprite, 60, 60, Sounds().return_dict_of_sounds())
hero.add(all_sprites)
draw_level("1", 32, 32, platform_sprites, all_sprites)
clock = pygame.time.Clock()
fps = 50
left_state, up_state = None, None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        up_state = -1
    if pygame.key.get_pressed()[pygame.K_a]:
        left_state = -1
    if pygame.key.get_pressed()[pygame.K_d]:
        left_state = 1
    if pygame.key.get_pressed()[pygame.K_r]:
        hero.reload()
    all_sprites.draw(screen)
    hero_sprite.update(platform_sprites, screen, left_state, up_state)
    camera.update(hero)
    for sprite in all_sprites:
        camera.apply(sprite)
    left_state, up_state = None, None
    clock.tick(fps)
    pygame.display.flip()
