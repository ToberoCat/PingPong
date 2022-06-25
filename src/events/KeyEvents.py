import pygame


def execute(events: list, *args):
    for event in events:
        event(*args)


class KeyListener:
    def __init__(self):
        self.on_key_down = []
        self.on_key_up = []
        self.exit = []

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execute(self.exit)
            elif event.type == pygame.KEYDOWN:
                execute(self.on_key_up, event.key)
            elif event.type == pygame.KEYUP:
                execute(self.on_key_down, event.key)
