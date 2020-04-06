import pygame
import Vars
import random


class Pipe:

    IMAGE = Vars.pipe_img

    def __init__(self, x):
        self.x = x
        self.img = [self.IMAGE, pygame.transform.rotate(self.IMAGE, 180)]
        self.gap = Vars.PIPE_GAP
        self.image_height = self.IMAGE.get_height()
        self.y = random.randint(30 + self.gap, Vars.WIN_HEIGHT - Vars.FLOOR_HEIGHT - 30)

    def draw(self):
        Vars.screen.blit(self.img[0], (self.x, self.y))
        Vars.screen.blit(self.img[1], (self.x, self.y - self.gap - self.image_height))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        pipe_mask = pygame.mask.from_surface(self.img[0])
        top_offset = (round(self.x - bird.x), round(self.y - self.image_height - self.gap - bird.y))
        bottom_offset = (round(self.x - bird.x), round(self.y - bird.y))
        if bird_mask.overlap(pipe_mask, top_offset) or bird_mask.overlap(pipe_mask, bottom_offset):
            Vars.lose = True

    def move(self):
        self.x -= Vars.FLOOR_VEL
