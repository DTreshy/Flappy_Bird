import pygame
import Vars


class LoopingImage:

    def __init__(self, altidute, image, velocity):
        self.image = image
        self.height = image.get_height()
        self.y = Vars.WIN_HEIGHT - altidute
        self.width = image.get_width()
        self.x = [0, self.width]
        self.velocity = velocity

    def draw(self):
        Vars.screen.blit(self.image, (self.x[0], self.y))
        Vars.screen.blit(self.image, (self.x[1], self.y))

    def move(self):
        self.x[0] -= self.velocity
        self.x[1] -= self.velocity
        for i in range (0, 2):
            if self.x[i] < -self.width:
                self.x[i] = self.width - 1


class Floor(LoopingImage):

    def collide(self, bird):
        bird_mask = bird.get_mask()
        floor_mask = pygame.mask.from_surface(self.image)
        offset = (-1, self.y - round(bird.y))
        if bird_mask.overlap(floor_mask, offset):
            Vars.running = False
