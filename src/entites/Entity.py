from src.data.ImageLoader import load_image


class Entity:
    def __init__(self, texture_path, width, height):
        self.x = 0
        self.y = 0
        self.image = load_image(texture_path, width, height)
    
    def tick(self):  # Abstract method
        pass

    def render(self):  # Abstract method
        pass


class Ball(Entity):
    def __init__(self):
        super
