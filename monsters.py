import os

import pygame
import pyganim
from funcs_for_load import load_image


ANIM_DELAY = 0.1

ANIM_RIGHT = [(pygame.transform.scale(pygame.image.load(os.path.join("data/wolf_anim/right", i)), (63, 33)),
               pygame.time.Clock().tick(20)) for i in os.listdir("data/wolf_anim/right")]

ANIM_LEFT = [(pygame.transform.scale(pygame.image.load(os.path.join("data/wolf_anim/left", i)), (63, 33)),
              pygame.time.Clock().tick(20)) for i in os.listdir("data/wolf_anim/left")]


class Monsters(pygame.sprite.Sprite):

    def __init__(self, group, x, y, max_x):
        super().__init__(group)
        self.rect = pygame.Rect(x, y, 63, 33)
        self.image = pygame.Surface((63, 33))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.Surface((63, 33), pygame.SRCALPHA, 32)
        self.boltAnimRight = pyganim.PygAnimation(ANIM_RIGHT)
        self.boltAnimRight.play()
        self.boltAnimLeft = pyganim.PygAnimation(ANIM_LEFT)
        self.boltAnimLeft.play()

        self.speed = 10
        self.startx, self.starty = x, y
        self.max_x = max_x

    def update(self, surface, platforms):
        if self.speed > 0:
            self.boltAnimRight.blit(surface, (0, 0))
        self.rect.x += self.speed
        self.collide(platforms)
        if abs(self.startx - self.rect.x) > self.max_x:
            self.speed = -self.speed

    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and self != p:
                self.speed = - self.speed
