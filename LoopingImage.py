import pygame
import Vars


class LoopingImage:

    def __init__(self, altidute, image, velocity):
        self.image = image
        self.altidute = altidute
        self.height = image.get_height()
        self.width = image.get_width()
        self.x = [0, self.width]
        self.velocity = velocity

    def draw(self):
        Vars.screen.blit(self.image, (self.x[0], -self.altidute))
        Vars.screen.blit(self.image, (self.x[1], -self.altidute))

    def move(self):
        self.x[0] -= 1
        self.x[1] -= 1
        for i in range (0, 2):
            if self.x[i] < -self.width:
                self.x[i] = self.width - 1


class Floor(LoopingImage):

    def collide(self):
        pass
