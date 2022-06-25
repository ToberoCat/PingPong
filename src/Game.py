import pygame

from src.events.KeyEvents import KeyListener
from src.world.World import World


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Init state
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.running = True

        # Create keylistener
        self.keylistener = KeyListener()
        self.keylistener.exit.append(self.quit_game)

        # Create world
        self.world = World(self.keylistener)

    def quit_game(self):
        self.running = False

    def create_render_loop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.tick()
            self.render()

            pygame.display.update()

    def render(self):
        self.world.render(self.screen)

    def tick(self):
        self.keylistener.listen()
        self.world.tick()


game = Game(640, 320)
game.create_render_loop()
