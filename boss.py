import os

import pygame
import pyganim

ANIMATION_RIGHT = [(pygame.transform.scale(pygame.image.load(os.path.join("data/Troll2/walk", i)), (300, 320)),
                    100)
                   for i in os.listdir("data/Troll2/walk")]

ANIMATION_LEFT = [(pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join("data/Troll2/walk", i)), (300, 320)), True, False), 100)
                     for i in os.listdir("data/Troll2/walk")] + [(pygame.transform.flip(pygame.transform.scale(
    pygame.image.load(os.path.join("data/Troll2/walk", i)), (300, 320)), True, False), 100)
                                                                    for i in os.listdir("data/Troll2/walk")][:-2:-1]

ANIMATION_STAY = [
    (pygame.transform.scale(pygame.image.load(os.path.join("data/Troll2/idle", i)), (300, 300)), 150)
    for i in os.listdir("data/Troll2/idle")]

GRAVITY = 0.5
SPEED = 5


class Troll(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        super().__init__(group)
        self.rect = pygame.Rect(x, y, 170, 290)
        self.image = pygame.Surface((170, 290), pygame.SRCALPHA, 32)
        self.rect.x, self.rect.y = x, y
        self.speed_y = 0
        self.speed_x = 0
        self.stay_anim = pyganim.PygAnimation(ANIMATION_STAY)
        self.stay_anim.play()
        self.right_anim = pyganim.PygAnimation(ANIMATION_RIGHT)
        self.right_anim.play()
        self.left_anim = pyganim.PygAnimation(ANIMATION_LEFT)
        self.left_anim.play()
        self.ground = False
        self.state = 1

    def collide_y(self, group):
        for sprite in group:
            if pygame.sprite.collide_rect(sprite, self):
                if self.speed_y > 0:
                    self.ground = True
                    self.speed_y = 0
                    self.rect.bottom = sprite.rect.top
            else:
                self.ground = False

    def update(self, collide_group, surface):
        if self.rect.colliderect((0, 0, 1920, 640)) == 1:
            if self.speed_x > 0:
                self.right_anim.blit(surface, (self.rect.x, self.rect.y))
            elif self.speed_x < 0:
                self.left_anim.blit(surface, (self.rect.x, self.rect.y))
            else:
                self.stay_anim.blit(surface, (self.rect.x, self.rect.y))

            self.speed_x = -SPEED

            if not self.ground:
                self.speed_y += GRAVITY

            self.rect.y += self.speed_y
            self.collide_y(collide_group)

            if self.state < 250:
                self.rect.x += self.speed_x
            else:
                self.speed_x = 0
                self.state = 250
            self.state += 1

    def reload(self):
        self.kill()
