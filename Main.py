import pygame
import Vars
import LoopingImage
import Pipe
from Bird import Bird


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.score = 0
        self.bird = Bird(60, 250)
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

    def draw(self):
        Vars.screen.fill(Vars.BLACK)
        self.bird.draw()
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    pygame.quit()
