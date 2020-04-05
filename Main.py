import pygame
import Vars
from LoopingImage import LoopingImage
import Pipe
from Bird import Bird


class Game:

    BACKGROUND_VEL = 10
    BIRD_X = 60
    BIRD_Y = 250

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.score = 0
        self.bird = Bird(self.BIRD_X, self.BIRD_Y)
        self.background = LoopingImage(0, Vars.background_img, self.BACKGROUND_VEL)
        self.fpsClock = pygame.time.Clock()

        while Vars.running:
            self.run()
            self.draw()
            self.fpsClock.tick(Vars.FPS)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Vars.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()
        self.bird.move()
        self.background.move()

    def draw(self):
        Vars.screen.fill(Vars.BLACK)
        self.background.draw()
        self.bird.draw()
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    pygame.quit()
