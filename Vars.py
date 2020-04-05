import pygame
import os


BLACK = (0, 0, 0)
WIN_HEIGHT = 900
WIN_WIDTH = 600
running = True
FPS = 50
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("Sprites","pipe.png")).convert_alpha())
background_img = pygame.transform.scale(pygame.image.load(os.path.join("Sprites","background.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("Sprites","bird" + str(x) + ".png"))) for x in range(1,5)]
Floor_img = pygame.transform.scale2x(pygame.image.load(os.path.join("Sprites","floor.png")).convert_alpha())
