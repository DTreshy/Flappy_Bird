import pygame
import Vars
from LoopingImage import LoopingImage, Floor
from Pipe import Pipe
from Bird import Bird


class Game:
    score_text = Vars.font1.render('Score', False, (0, 0, 0))

    def __init__(self):
        self.bird = Bird(Vars.BIRD_START_X, Vars.BIRD_START_Y)
        self.pipe = [Pipe(Vars.PIPE_STARTING_X + i * (Vars.PIPE_DISTANCE + Pipe.WIDTH)) for i in range(0, 3)]
        self.background = LoopingImage(Vars.WIN_HEIGHT, Vars.background_img, Vars.BACKGROUND_VEL)
        self.floor = Floor(Vars.FLOOR_HEIGHT, Vars.Floor_img, Vars.FLOOR_VEL)
        self.fpsClock = pygame.time.Clock()
        self.distance = 0
        self.score = 0
        self.score_number_text = Vars.font1.render(str(self.score), False, (0, 0, 0))

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
        self.add_score()
        if self.pipe[0].x < 0 - self.pipe[0].IMAGE.get_width():
            self.pipe.pop(0)
            self.pipe.append(Pipe(self.pipe[-1].x + Pipe.WIDTH + Vars.PIPE_DISTANCE))
        if Vars.lose:
            self.lose()

    def draw(self):
        Vars.screen.fill(Vars.BLACK)
        self.background.draw()
        for i in self.pipe:
            i.draw()
        self.floor.draw()
        self.bird.draw()
        Vars.screen.blit(self.score_text, (450, 30))
        Vars.screen.blit(self.score_number_text, (580, 30))
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Vars.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def add_score(self):
        self.distance += Vars.FLOOR_VEL
        if self.score == 0 and self.distance > Vars.PIPE_STARTING_X + (Pipe.WIDTH / 2) - Vars.BIRD_START_X:
            self.score += 1
            self.distance -= Vars.PIPE_STARTING_X + (Pipe.WIDTH / 2) - Vars.BIRD_START_X
        elif self.score > 0 and self.distance > Vars.PIPE_DISTANCE + Pipe.WIDTH:
            self.score += 1
            self.distance -= Vars.PIPE_DISTANCE + Pipe.WIDTH

        score_str = str(self.score)
        for i in range(0, 3):
            if score_str.__len__() < 4:
                score_str = '0' + score_str

        self.score_number_text = Vars.font1.render(score_str, False, (0, 0, 0))

    def lose(self):
        self.bird = Bird(Vars.BIRD_START_X, Vars.BIRD_START_Y)
        self.pipe = self.pipe = [Pipe(Vars.PIPE_STARTING_X + i * (Vars.PIPE_DISTANCE + Pipe.WIDTH)) for i in range(0, 3)]
        self.background = LoopingImage(Vars.WIN_HEIGHT, Vars.background_img, Vars.BACKGROUND_VEL)
        self.floor = Floor(Vars.FLOOR_HEIGHT, Vars.Floor_img, Vars.FLOOR_VEL)
        self.score = 0
        self.distance = 0
        Vars.lose = False


if __name__ == "__main__":
    game = Game()
    pygame.quit()
