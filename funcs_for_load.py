import os

import pygame

pygame.display.init()
size = width, height = 800, 640
pygame.display.set_mode(size)


def load_image(filename, colorkey=None):
    fullname = os.path.join('data', filename)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', filename)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image
