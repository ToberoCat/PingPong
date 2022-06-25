import pygame


class KeyListener:
    def __init__(self):
        self.on_key_down = []
        self.on_key_up = []
        self.exit = []

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for e in self.exit:
                    e()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                for e in self.on_key_down:
                    e(event)
            elif event.type == pygame.KEYUP:
                for e in self.on_key_up:
                    e(event)

