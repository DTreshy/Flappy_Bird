import pygame
import math
import Vars


def blitRotateCenter(surf, image, topleft, angle):
    """
    Rotate a surface and blit it to the window
    :param surf: the surface to blit to
    :param image: the image surface to rotate
    :param topleft: the top left position of the image
    :param angle: a float value for angle
    :return: None
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)


class Bird:

    IMAGES = Vars.bird_images
    MAX_ROTATION = 28
    ANIMATION_TIME = 5
    ROTATION_VEL = 20
    MAX_VELOCITY = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.cur_rotation = 0
        self.tick_count = 0
        self.cur_image = 0
        self.img = self.IMAGES[self.cur_image]
        self.animation_timer = 0

    def draw(self):
        self.animation_timer += 1
        self.cur_image = math.floor(self.animation_timer / self.ANIMATION_TIME)
        if self.cur_image == len(self.IMAGES):
            self.cur_image = 0
            self.animation_timer = 0
        self.rotate()
        self.img = self.IMAGES[self.cur_image]
        blitRotateCenter(Vars.screen, self.img, (self.x, self.y), self.cur_rotation)

    def rotate(self):
        self.cur_rotation = self.velocity * -3.8
        if self.cur_rotation > self.MAX_ROTATION:
            self.cur_rotation = self.MAX_ROTATION
        elif self.cur_rotation <= -60:
            self.cur_rotation = -60
            self.cur_image = 1

    def move(self):
        self.tick_count += 1
        self.velocity += 0.01 * self.tick_count ** 1.9
        if self.velocity > self.MAX_VELOCITY:
            self.velocity = self.MAX_VELOCITY
        self.y += self.velocity

    def jump(self):
        self.velocity = -self.MAX_VELOCITY + 2
        self.tick_count = 0

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
