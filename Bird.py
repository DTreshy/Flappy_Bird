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

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.cur_rotation = 0
        self.tick_count = 0
        self.cur_image = 0
        self.img = self.IMAGES[self.cur_image]
        self.animation_timer = 0
        self.max_up_rotation = Vars.BIRD_MAX_UP_ROTATION
        self.max_down_rotation = Vars.BIRD_MAX_DOWN_ROTATION
        self.animation_time = Vars.BIRD_ANIMATION_TIME
        self.rotation_vel = Vars.BIRD_ROTATION_VEL
        self.max_velocity = Vars.BIRD_MAX_VELOCITY

    def draw(self):
        self.animation_timer += 1
        self.cur_image = math.floor(self.animation_timer / self.animation_time)
        if self.cur_image == len(self.IMAGES):
            self.cur_image = 0
            self.animation_timer = 0
        self.rotate()
        self.img = self.IMAGES[self.cur_image]
        blitRotateCenter(Vars.screen, self.img, (self.x, self.y), self.cur_rotation)

    def rotate(self):
        self.cur_rotation = self.velocity * -self.rotation_vel
        if self.cur_rotation > self.max_up_rotation:
            self.cur_rotation = self.max_up_rotation
        elif self.cur_rotation <= -self.max_down_rotation:
            self.cur_rotation = -self.max_down_rotation
            self.cur_image = 1

    def move(self):
        self.tick_count += 1
        self.velocity += 0.01 * self.tick_count ** 1.9
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity
        self.y += self.velocity
        if self.y < 0:
            self.y = 0

    def jump(self):
        self.velocity = -self.max_velocity + 2
        self.tick_count = 0

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
