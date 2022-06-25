from src.data.ImageLoader import load_image


class Entity:
    def __init__(self, texture_path, width, height):
        self.x = 0
        self.y = 0
        self.image = load_image(texture_path, width, height)

    def key_down(self, key):  # Abstract method
        pass

    def key_up(self, key):  # Abstract method
        pass

    def mouse_up(self, button):
        pass

    def mouse_down(self, button):
        pass

    def tick(self):  # Abstract method
        pass

    def render(self, scene):  # Abstract method
        pass
