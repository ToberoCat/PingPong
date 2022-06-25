import pygame

from src.data.ImageLoader import load_image


class Entity:
    def __init__(self, texture_path, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.image = load_image(texture_path, width, height)

    def key_down(self, key):  # Abstract method
        pass

    def key_up(self, key):  # Abstract method
        pass

    def mouse_up(self, button):  # Abstract method
        pass

    def mouse_down(self, button):  # Abstract method
        pass

    def get_bounding_box(self):
        return pygame.Rect(0, 0, self.width, self.height)

    def tick(self):  # Abstract method
        pass

    def render(self, scene):  # Abstract method
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        scene.blit(self.image, rect)
