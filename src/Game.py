import pygame


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

        self.width = width
        self.height = height
        # Open window

        while True:
            self.screen.fill((255, 0, 0))
            pygame.display.update()

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
