import os

import pygame


class Platform(pygame.sprite.Sprite):
    image_platform = pygame.image.load("data/tile.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Platform.image_platform
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class InvisiblePlatform(pygame.sprite.Sprite):
    image_platform = pygame.image.load("data/tile.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.Surface((50, 64), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class LeftPlatform(pygame.sprite.Sprite):
    image_platform = pygame.image.load("data/tilel.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = LeftPlatform.image_platform
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class RightPlatform(pygame.sprite.Sprite):
    image_platform = pygame.image.load("data/tiler.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = RightPlatform.image_platform
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Sign(pygame.sprite.Sprite):
    image_platform = pygame.image.load("data/sign.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Sign.image_platform
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
            elif level[y][x] == "?":
                InvisiblePlatform(group_of_sprites, platfrom_w * x, platfrom_h * y).add(group_of_sprites_2)
            elif level[y][x] == "l":
                LeftPlatform(group_of_sprites, platfrom_w * x, platfrom_h * y).add(group_of_sprites_2)
            elif level[y][x] == "r":
                RightPlatform(group_of_sprites, platfrom_w * x, platfrom_h * y).add(group_of_sprites_2)
            elif level[y][x] == "s":
                Sign(group_of_sprites, platfrom_w * x, platfrom_h * y).add(group_of_sprites_2)
