import pygame

from src.world.World import World


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.world = World()
        self.running = True

    def create_render_loop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.tick()
            self.render()

            pygame.display.update()

    def render(self):
        self.world.render(self.screen)

    def tick(self):
        self.world.tick()


game = Game(640, 320)
game.create_render_loop()
