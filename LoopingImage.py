import pygame
import Vars


class LoopingImage:

    def __init__(self, altidute, image, velocity):
        self.image = image
        self.height = image.get_height()
        self.y = Vars.WIN_HEIGHT - altidute
        self.width = image.get_width()
        self.x = [0, self.width, 2 * self.width]
        self.velocity = velocity

    def draw(self):
        for i in range(0, self.x.__len__()):
            Vars.screen.blit(self.image, (round(self.x[i]), self.y))

    def move(self):
        for i in range(0, self.x.__len__()):
            self.x[i] -= self.velocity
            if self.x[i] <= -self.width:
                self.x[i] = self.x[i - 1] + self.width - 5


class Floor(LoopingImage):

    def collide(self, bird):
        bird_mask = bird.get_mask()
        floor_mask = pygame.mask.from_surface(self.image)
        offset = (-1, self.y - round(bird.y))
        if bird_mask.overlap(floor_mask, offset):
            Vars.lose = True
