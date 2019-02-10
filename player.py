import os

import pygame
import pyganim

GRAVITY = 0.3
SPEED = 5
JUMP = 10

ANIMATION_RIGHT = [('data/black_knight/walk_1.png', 100),
                   ('data/black_knight/walk_2.png', 100),
                   ('data/black_knight/walk_3.png', 100),
                   ('data/black_knight/walk_4.png', 100)]

ANIMATION_JUMP = [('data/black_knight/jump_2.png', 3000)]

ANIMATION_STAY = [('data/black_knight/idle_1.png', 1)]

ANIMATION_JUMP_LEFT = [('data/black_knight/jump_2.png', 100)]

ANIMATION_JUMP_RIGHT = [('data/black_knight/jump_2.png', 100)]


class Hero(pygame.sprite.Sprite):
    def __init__(self, group, x, y, sounds):
        super().__init__(group)
        self.sounds = sounds
        self.speed_x, self.speed_y = 0, 0
        self.rect = pygame.Rect(x, y, 50, 64)
        self.image = pygame.Surface((50, 64))
        self.start_pos = (x, y)
        self.ground = False
        self.right_anim = pyganim.PygAnimation(ANIMATION_RIGHT)
        self.right_anim.play()
        self.stay_anim = pyganim.PygAnimation(ANIMATION_STAY)
        self.stay_anim.play()
        self.jump_anim = pyganim.PygAnimation(ANIMATION_JUMP)
        self.jump_anim.play()
        self.rect.x, self.rect.y = x, y

    def collision_y(self, sprites_group):
        for sprite in sprites_group:
            if pygame.sprite.collide_rect(sprite, self):
                if self.speed_y > 0:
                    self.ground = True
                    self.speed_y = 0
                    self.rect.bottom = sprite.rect.top
                if self.speed_y < 0:
                    self.speed_y = 0
                    self.rect.top = sprite.rect.bottom

    def collision_x(self, sprites_group):
        for sprite in sprites_group:
            if pygame.sprite.collide_rect(sprite, self):
                if self.speed_x > 0:
                    self.rect.right = sprite.rect.left
                if self.speed_x < 0:
                    self.rect.left = sprite.rect.right

    def update(self, group, surface, left=None, up=None):
        if left is not None:
            self.speed_x = left * SPEED
            if self.ground:
                self.sounds["walk"].stop()
                self.right_anim.blit(surface, (self.rect.x, self.rect.y))
                self.sounds["walk"].play()
            else:
                self.jump_anim.blit(surface, (self.rect.x, self.rect.y))

        else:
            self.speed_x = 0
        if up is not None and self.ground:
            self.sounds["jump"].stop()
            self.ground = False
            self.speed_y = up * JUMP
            self.sounds["jump"].play()
        else:
            self.speed_y += GRAVITY

        if left is None and up is None and self.ground:
            self.stay_anim.blit(surface, (self.rect.x, self.rect.y))
        if not self.ground:
            self.jump_anim.blit(surface, (self.rect.x, self.rect.y))

        self.rect.y += self.speed_y
        self.collision_y(group)

        self.rect.x += self.speed_x
        self.collision_x(group)

    def reload(self):
        self.rect.x, self.rect.y = self.start_pos[0], self.start_pos[1]
        self.speed_x, self.speed_y = 0, 0
