import pygame
import Vars
from LoopingImage import LoopingImage, Floor
from Pipe import Pipe
from Bird import Bird


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Vars.CAPTION)
        self.bird = Bird(Vars.BIRD_START_X, Vars.BIRD_START_Y)
        self.pipe = [Pipe(Vars.PIPE_STARTING_X), Pipe(Vars.PIPE_STARTING_X + Vars.PIPE_STARTING_X),
                     Pipe(Vars.PIPE_STARTING_X + 2 * Vars.PIPE_STARTING_X)]
        self.background = LoopingImage(Vars.WIN_HEIGHT, Vars.background_img, Vars.BACKGROUND_VEL)
        self.floor = Floor(Vars.FLOOR_HEIGHT, Vars.Floor_img, Vars.FLOOR_VEL)
        self.fpsClock = pygame.time.Clock()

        while Vars.running:
            self.run()
            self.draw()
            self.fpsClock.tick(Vars.FPS)

    def run(self):
        self.events()
        self.bird.move()
        self.background.move()
        self.floor.move()
        for i in self.pipe:
            i.move()
            i.collide(self.bird)
        self.floor.collide(self.bird)
        self.addScore()
        if self.pipe[0].x < 0 - self.pipe[0].IMAGE.get_width():
            self.pipe.pop(0)
            self.pipe.append(Pipe(self.pipe[-1].x + self.pipe[0].IMAGE.get_width() + Vars.PIPE_DISTANCE))
        if Vars.lose:
            self.lose()

    def draw(self):
        Vars.screen.fill(Vars.BLACK)
        self.background.draw()
        for i in self.pipe:
            i.draw()
        self.floor.draw()
        self.bird.draw()
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Vars.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def addScore(self):
        for i in self.pipe:
            pass

    def lose(self):
        self.bird = Bird(Vars.BIRD_START_X, Vars.BIRD_START_Y)
        self.pipe = [Pipe(Vars.PIPE_STARTING_X), Pipe(Vars.PIPE_STARTING_X + Vars.PIPE_STARTING_X),
                     Pipe(Vars.PIPE_STARTING_X + 2 * Vars.PIPE_STARTING_X)]
        self.background = LoopingImage(Vars.WIN_HEIGHT, Vars.background_img, Vars.BACKGROUND_VEL)
        self.floor = Floor(Vars.FLOOR_HEIGHT, Vars.Floor_img, Vars.FLOOR_VEL)
        Vars.score = 0
        Vars.lose = False


if __name__ == "__main__":
    game = Game()
    pygame.quit()
