import pygame
import time

from src.entites.Ball import Ball
from src.events.KeyEvents import KeyListener
from src.world.World import World

FPS = 60


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
        self.world.register_entity(Ball(width, height))

    def quit_game(self):
        self.running = False

    def create_render_loop(self):
        time_per_tick = 1000000000 / FPS
        delta = 0
        last_time = time.time_ns()
        timer = 0
        ticks = 0

        while self.running:
            now = time.time_ns()
            delta += (now - last_time) / time_per_tick
            timer += now - last_time
            last_time = now

            if delta >= 1:
                self.tick()
                self.render()

                ticks += 1
                delta -= 1

                pygame.display.update()

            if timer >= 1000000000:
                #print(f"Ticks: {ticks}")
                ticks = 0
                timer = 0

    def render(self):
        self.screen.fill((0, 0, 0))
        self.world.render(self.screen)

    def tick(self):
        self.keylistener.listen()
        self.world.tick()


game = Game(640, 320)
game.create_render_loop()
