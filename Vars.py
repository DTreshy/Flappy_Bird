import pygame
import os


BLACK = (0, 0, 0)
WIN_HEIGHT = 900
WIN_WIDTH = 700
running = True
lose = False
FPS = 50
BACKGROUND_VEL = 2
PIPE_GAP = 400
PIPE_STARTING_X = 800
PIPE_DISTANCE = 350
FLOOR_VEL = 7.2
FLOOR_HEIGHT = 120
BIRD_START_X = 60
BIRD_START_Y = 250
CAPTION = "Flappy Bird"
BIRD_MAX_UP_ROTATION = 28
BIRD_MAX_DOWN_ROTATION = 60
BIRD_ANIMATION_TIME = 4
BIRD_ROTATION_VEL = 3.5
BIRD_MAX_VELOCITY = 20
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("Sprites", "pipe.png")).convert_alpha())
background_img = pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "background.png")).convert_alpha(),
                                        (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("Sprites", "bird" + str(x) + ".png")))
               for x in range(1, 5)]
Floor_img = pygame.transform.scale2x(pygame.image.load(os.path.join("Sprites", "floor.png")).convert_alpha())
