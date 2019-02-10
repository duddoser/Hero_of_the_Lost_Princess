import os

import pygame

from funcs_for_load import load_image


class Platform(pygame.sprite.Sprite):
    image_platform = load_image("tile.png", -1)

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Platform.image_platform
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


def draw_level(filename, platfrom_h, platfrom_w, group_of_sprites, group_of_sprites_2):
    fullname = os.path.join('data/levels', "{}.txt".format(filename))
    with open(fullname, mode="r") as level_in:
        level = [i.rstrip() for i in level_in.readlines()]
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == "-":
                Platform(group_of_sprites, platfrom_w * x, platfrom_h * y).add(group_of_sprites_2)
