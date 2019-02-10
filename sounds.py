import os

import pygame

pygame.mixer.init()


class Sounds(object):

    def __init__(self):
        self.directory = "data/music/"

    def return_dict_of_sounds(self):
        dictionary_of_sounds = dict()
        for file in os.listdir(self.directory):
            dictionary_of_sounds[file[:file.rfind(".")]] =\
                pygame.mixer.Sound(os.path.join(self.directory, file))
        return dictionary_of_sounds


if __name__ == '__main__':
    print(Sounds().return_dict_of_sounds())
