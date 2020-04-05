import pygame
import Vars


class LoopingImage:

    def __init__(self, altidute, image):
        self.image = image
        self.altidute = altidute
        self.height = image.get_height()
        self.x = [0, image.get_width()]

    def draw(self):
        pass

    def move(self):
        pass


class Floor(LoopingImage):

    def collide(self):
        pass
