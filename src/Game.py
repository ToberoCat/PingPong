import pygame

TILE_WIDTH = 32  # Pixels width per image
TILE_HEIGHT = 32  # Pixels height per image


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

        self.width = width
        self.height = height
        # Open window

        self.screen.fill((32, 64, 64))
        while True:
            pass

    def create_render_loop(self):
        # Create loop that

        pass

    def render(self, scene):
        # Draw the shapes
        pass

    def tick(self):
        # Calculate the actions
        pass


game = Game(640, 320)
